import datetime as dt

import pytest
from django.utils import timezone

from registry.constants import RegistryV2ExportState, RegistryV2ExportType, RegistryV2Format

from ..factories import RegistryV2ExportFactory
from ..models import RegistryV2Export

pytestmark = pytest.mark.django_db


@pytest.fixture
def create_exports():
    def _create_exports():
        now = timezone.now()

        five_days_ago_export = RegistryV2ExportFactory(
            siret="12345678900001",
            registry_type=RegistryV2ExportType.INCOMING,
            export_format=RegistryV2Format.CSV,
            start_date=now - dt.timedelta(days=30),
            end_date=now,
            created_at=now - dt.timedelta(days=5),
        )

        three_days_ago_export = RegistryV2ExportFactory(
            siret="12345678900002",
            registry_type=RegistryV2ExportType.OUTGOING,
            start_date=now - dt.timedelta(days=30),
            end_date=now,
            state=RegistryV2ExportState.PENDING,
            created_at=now - dt.timedelta(days=3),
        )

        one_day_ago_export = RegistryV2ExportFactory(
            siret="12345678900003",
            start_date=now - dt.timedelta(days=30),
            end_date=now,
            state=RegistryV2ExportState.STARTED,
            waste_types_texs=True,
            created_at=now - dt.timedelta(days=1),
        )

        today_export = RegistryV2ExportFactory(
            siret="12345678900004",
            start_date=now - dt.timedelta(days=30),
            end_date=now,
            state=RegistryV2ExportState.FAILED,
            waste_types_dnd=True,
            created_at=now,
        )

        return {
            "five_days_ago": five_days_ago_export,
            "three_days_ago": three_days_ago_export,
            "one_day_ago": one_day_ago_export,
            "today": today_export,
        }

    return _create_exports


def test_recent_default_days(create_exports):
    exports = create_exports()

    recent_exports = RegistryV2Export.objects.recent()

    assert recent_exports.count() == 2
    assert exports["today"] in recent_exports
    assert exports["one_day_ago"] in recent_exports
    assert exports["three_days_ago"] not in recent_exports
    assert exports["five_days_ago"] not in recent_exports


def test_recent_custom_days(create_exports):
    exports = create_exports()

    recent_exports = RegistryV2Export.objects.recent(days_ago=4)

    assert recent_exports.count() == 3
    assert exports["today"] in recent_exports
    assert exports["one_day_ago"] in recent_exports
    assert exports["three_days_ago"] in recent_exports
    assert exports["five_days_ago"] not in recent_exports


def test_recent_with_no_days(create_exports):
    create_exports()

    recent_exports = RegistryV2Export.objects.recent(days_ago=0)

    assert recent_exports.count() == 0


def test_recent_with_all_days(create_exports):
    exports = create_exports()

    recent_exports = RegistryV2Export.objects.recent(days_ago=10)

    assert recent_exports.count() == 4
    assert exports["today"] in recent_exports
    assert exports["one_day_ago"] in recent_exports
    assert exports["three_days_ago"] in recent_exports
    assert exports["five_days_ago"] in recent_exports


def test_recent_with_empty_db():
    recent_exports = RegistryV2Export.objects.recent()

    assert recent_exports.count() == 0


def test_recent_chaining_with_other_filters(create_exports):
    exports = create_exports()

    recent_pending_exports = RegistryV2Export.objects.recent(days_ago=4).filter(state=RegistryV2ExportState.PENDING)

    assert recent_pending_exports.count() == 1
    assert exports["three_days_ago"] in recent_pending_exports
