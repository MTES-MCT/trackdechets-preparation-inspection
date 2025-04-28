import pytest

from ..factories import RegistryV2ExportFactory

pytestmark = pytest.mark.django_db


def test_registry_v2_export_factory():
    registry = RegistryV2ExportFactory()
    assert registry.id
