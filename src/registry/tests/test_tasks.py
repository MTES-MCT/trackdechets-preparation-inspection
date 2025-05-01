from unittest.mock import patch

import pytest

from registry.constants import RegistryV2ExportState
from registry.task import refresh_registry_export

from ..factories import RegistryV2ExportFactory
from ..task import generate_registry_export

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_generate_registry_export_success():
    registry_export = RegistryV2ExportFactory()
    mock_response = {
        "data": {
            "generateRegistryV2Export": {
                "id": "mock-export-id-123",
                "status": RegistryV2ExportState.STARTED,
            }
        }
    }

    with patch("httpx.Client.post") as mock_post:
        mock_post.return_value.json.return_value = mock_response

        generate_registry_export(registry_export.pk)

        registry_export.refresh_from_db()

        assert registry_export.registry_export_id == "mock-export-id-123"
        assert registry_export.state == RegistryV2ExportState.STARTED

        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args.kwargs

        assert call_kwargs["url"] == "https://testapi.test"
        assert call_kwargs["headers"]["Authorization"] == "Bearer thetoken"

        request_payload = call_kwargs["json"]
        variables = request_payload["variables"]
        assert variables["siret"] == registry_export.siret
        assert variables["registryType"] == registry_export.registry_type
        assert variables["format"] == registry_export.export_format


@pytest.mark.django_db
def test_generate_registry_export_api_error():
    registry_export = RegistryV2ExportFactory()

    mock_error_response = {"errors": [{"message": "Export generation failed"}]}

    with patch("httpx.Client.post") as mock_post:
        # Configure the mock to return an error response
        mock_post.return_value.json.return_value = mock_error_response

        generate_registry_export(registry_export.pk)

        registry_export.refresh_from_db()

        assert registry_export.registry_export_id == ""
        assert registry_export.state == RegistryV2ExportState.PENDING


@pytest.mark.django_db
def test_generate_registry_export_request_exception():
    registry_export = RegistryV2ExportFactory()
    with patch("httpx.Client.post") as mock_post:
        mock_post.side_effect = Exception("Network error")

        with pytest.raises(Exception):
            generate_registry_export(registry_export.pk)

        registry_export.refresh_from_db()

        assert registry_export.registry_export_id == ""
        assert registry_export.state == RegistryV2ExportState.PENDING


@pytest.mark.django_db
def test_refresh_registry_export_success():
    registry_export = RegistryV2ExportFactory(registry_export_id="wxcvbn")
    mock_response = {
        "data": {
            "registryV2Export": {
                "id": "existing-export-id-123",
                "status": RegistryV2ExportState.SUCCESSFUL,
            }
        }
    }

    with patch("httpx.Client.post") as mock_post:
        mock_post.return_value.json.return_value = mock_response

        refresh_registry_export(registry_export.pk)

        registry_export.refresh_from_db()

        assert registry_export.state == RegistryV2ExportState.SUCCESSFUL

        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args.kwargs

        assert call_kwargs["url"] == "https://testapi.test"
        assert call_kwargs["headers"]["Authorization"] == "Bearer thetoken"

        request_payload = call_kwargs["json"]
        assert request_payload["variables"]["id"] == registry_export.registry_export_id


@pytest.mark.django_db
def test_refresh_registry_export_in_progress():
    registry_export = RegistryV2ExportFactory(registry_export_id="wxcvbn")
    mock_response = {
        "data": {
            "registryV2Export": {
                "id": "existing-export-id-123",
                "status": RegistryV2ExportState.STARTED,
            }
        }
    }

    with patch("httpx.Client.post") as mock_post:
        mock_post.return_value.json.return_value = mock_response

        refresh_registry_export(registry_export.pk)

        registry_export.refresh_from_db()

        assert registry_export.state == RegistryV2ExportState.STARTED


@pytest.mark.django_db
def test_refresh_registry_export_failed():
    registry_export = RegistryV2ExportFactory(registry_export_id="wxcvbn")
    mock_response = {
        "data": {
            "registryV2Export": {
                "id": "existing-export-id-123",
                "status": RegistryV2ExportState.FAILED,
            }
        }
    }

    with patch("httpx.Client.post") as mock_post:
        mock_post.return_value.json.return_value = mock_response

        refresh_registry_export(registry_export.pk)

        registry_export.refresh_from_db()

        assert registry_export.state == RegistryV2ExportState.FAILED


@pytest.mark.django_db
def test_refresh_registry_export_request_exception():
    registry_export = RegistryV2ExportFactory(registry_export_id="wxcvbn")

    with patch("httpx.Client.post") as mock_post:
        mock_post.side_effect = Exception("Network error")

        with pytest.raises(Exception):
            refresh_registry_export(registry_export.pk)

        registry_export.refresh_from_db()

        assert registry_export.state == RegistryV2ExportState.PENDING
