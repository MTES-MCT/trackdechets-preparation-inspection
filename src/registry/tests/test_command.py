import datetime as dt
from unittest.mock import patch

import pytest
from django.core.management import call_command
from django.utils import timezone

from ..constants import RegistryV2ExportState
from ..factories import RegistryV2ExportFactory
from ..models import RegistryV2Export


@pytest.fixture
def setup_registry_exports():
    now = timezone.now()

    # Recent pending export with ID (should be refreshed)
    recent_pending_with_id = RegistryV2ExportFactory(
        siret="12345678900001",
        state=RegistryV2ExportState.PENDING,
        waste_types_dnd=True,
        created_at=now - dt.timedelta(minutes=30),
        registry_export_id="export-id-1",
    )

    # Recent started export with ID (should be refreshed)
    recent_started_with_id = RegistryV2ExportFactory(
        siret="12345678900002",
        state=RegistryV2ExportState.STARTED,
        waste_types_dnd=True,
        created_at=now - dt.timedelta(minutes=45),
        registry_export_id="export-id-2",
    )

    # Recent pending export without ID but not old enough (nothing should happen)
    recent_pending_no_id = RegistryV2ExportFactory(
        siret="12345678900003",
        state=RegistryV2ExportState.PENDING,
        waste_types_dnd=True,
        created_at=now - dt.timedelta(minutes=30),
        registry_export_id="",
    )

    # Old pending export without ID (should be marked as failed)
    old_pending_no_id = RegistryV2ExportFactory(
        siret="12345678900004",
        state=RegistryV2ExportState.PENDING,
        waste_types_dnd=True,
        created_at=now - dt.timedelta(hours=2),
        registry_export_id="",
    )

    # Completed export (should be ignored)
    completed_export = RegistryV2ExportFactory(
        siret="12345678900005",
        state=RegistryV2ExportState.SUCCESSFUL,
        waste_types_dnd=True,
        created_at=now - dt.timedelta(hours=1),
        registry_export_id="export-id-3",
    )

    # Old export but with a completed state (should be ignored)
    old_completed_export = RegistryV2ExportFactory(
        siret="12345678900006",
        state=RegistryV2ExportState.SUCCESSFUL,
        waste_types_dnd=True,
        created_at=now - dt.timedelta(days=5),
        registry_export_id="export-id-4",
    )

    return {
        "recent_pending_with_id": recent_pending_with_id,
        "recent_started_with_id": recent_started_with_id,
        "recent_pending_no_id": recent_pending_no_id,
        "old_pending_no_id": old_pending_no_id,
        "completed_export": completed_export,
        "old_completed_export": old_completed_export,
    }


@pytest.mark.django_db
def test_refresh_states_command(setup_registry_exports):
    with patch("registry.task.refresh_registry_export.delay") as mock_delay:
        call_command("refresh_export_states", duration=1)

        assert mock_delay.call_count == 2
        mock_delay.assert_any_call(setup_registry_exports["recent_pending_with_id"].pk)
        mock_delay.assert_any_call(setup_registry_exports["recent_started_with_id"].pk)

        old_pending = setup_registry_exports["old_pending_no_id"]
        old_pending.refresh_from_db()
        assert old_pending.state == RegistryV2ExportState.FAILED


@pytest.mark.django_db
def test_refresh_states_command_with_no_exports():
    with patch("registry.task.refresh_registry_export.delay") as mock_delay:
        call_command("refresh_export_states", duration=1)

        mock_delay.assert_not_called()


@pytest.mark.django_db
def test_refresh_states_command_only_processes_recent_exports(setup_registry_exports):
    old_export = RegistryV2ExportFactory(
        siret="12345678900007",
        state=RegistryV2ExportState.PENDING,
        waste_types_dnd=True,
        created_at=timezone.now() - dt.timedelta(days=5),  # Older than the recent() cutoff
        registry_export_id="export-id-5",
    )

    with patch("registry.models.RegistryV2ExportQuerySet.recent") as mock_recent:
        mock_recent.return_value = RegistryV2Export.objects.filter(
            pk__in=[
                setup_registry_exports["recent_pending_with_id"].pk,
                setup_registry_exports["recent_started_with_id"].pk,
            ]
        )

        with patch("registry.task.refresh_registry_export.delay") as mock_delay:
            call_command("refresh_export_states", duration=1)

            mock_recent.assert_called_once()

            assert mock_delay.call_count == 2
            mock_delay.assert_any_call(setup_registry_exports["recent_pending_with_id"].pk)
            mock_delay.assert_any_call(setup_registry_exports["recent_started_with_id"].pk)

            assert old_export.pk not in [call_args[0][0] for call_args in mock_delay.call_args_list]
