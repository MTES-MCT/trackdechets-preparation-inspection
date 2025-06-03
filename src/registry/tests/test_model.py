from datetime import datetime

import pytest

from ..constants import RegistryV2DeclarationType, RegistryV2ExportType, RegistryV2Format
from ..factories import RegistryV2ExportFactory

pytestmark = pytest.mark.django_db


def test_get_gql_variables_minimal_required_fields():
    export = RegistryV2ExportFactory(
        siret="12345678901234",
        registry_type=RegistryV2ExportType.INCOMING,
        export_format=RegistryV2Format.CSV,
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2023, 12, 31),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=False,
        waste_types_dd=False,
        waste_types_texs=False,
        waste_codes=[],
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "12345678901234",
        "registryType": RegistryV2ExportType.INCOMING,
        "format": RegistryV2Format.CSV,
        "dateRange": {"_gte": "2023-01-01T00:00:00", "_lte": "2023-12-31T00:00:00"},
        "where": {"declarationType": {"_eq": RegistryV2DeclarationType.ALL}},
    }
    assert variables == expected


def test_get_gql_variables_with_single_waste_type():
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.OUTGOING,
        export_format=RegistryV2Format.XLSX,
        start_date=datetime(2023, 6, 1),
        end_date=datetime(2023, 6, 30),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=True,
        waste_types_dd=False,
        waste_types_texs=False,
        waste_codes=[],
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.OUTGOING,
        "format": RegistryV2Format.XLSX,
        "dateRange": {"_gte": "2023-06-01T00:00:00", "_lte": "2023-06-30T00:00:00"},
        "where": {"declarationType": {"_eq": RegistryV2DeclarationType.ALL}, "wasteType": {"_in": ["DND"]}},
    }
    assert variables == expected


def test_get_gql_variables_with_multiple_waste_types():
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.INCOMING,
        export_format=RegistryV2Format.CSV,
        start_date=datetime(2023, 3, 15),
        end_date=datetime(2023, 3, 16),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=True,
        waste_types_dd=True,
        waste_types_texs=False,
        waste_codes=[],
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.INCOMING,
        "format": RegistryV2Format.CSV,
        "dateRange": {"_gte": "2023-03-15T00:00:00", "_lte": "2023-03-16T00:00:00"},
        "where": {"declarationType": {"_eq": RegistryV2DeclarationType.ALL}, "wasteType": {"_in": ["DND", "DD"]}},
    }
    assert variables == expected


def test_get_gql_variables_with_all_waste_types():
    """Test with all waste types enabled."""
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.OUTGOING,
        export_format=RegistryV2Format.XLSX,
        start_date=datetime(2023, 12, 1),
        end_date=datetime(2023, 12, 31),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=True,
        waste_types_dd=True,
        waste_types_texs=True,
        waste_codes=[],
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.OUTGOING,
        "format": RegistryV2Format.XLSX,
        "dateRange": {"_gte": "2023-12-01T00:00:00", "_lte": "2023-12-31T00:00:00"},
        "where": {
            "declarationType": {"_eq": RegistryV2DeclarationType.ALL},
            "wasteType": {"_in": ["DND", "DD", "TEXS"]},
        },
    }
    assert variables == expected


def test_get_gql_variables_with_waste_codes():
    waste_codes = ["01 03 05*", "01 03 07*", "01 03 10*"]
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.INCOMING,
        export_format=RegistryV2Format.CSV,
        start_date=datetime(2023, 5, 10),
        end_date=datetime(2023, 5, 20),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=False,
        waste_types_dd=False,
        waste_types_texs=False,
        waste_codes=waste_codes,
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.INCOMING,
        "format": RegistryV2Format.CSV,
        "dateRange": {"_gte": "2023-05-10T00:00:00", "_lte": "2023-05-20T00:00:00"},
        "where": {
            "declarationType": {"_eq": RegistryV2DeclarationType.ALL},
            "wasteCode": {"_in": ["01 03 05*", "01 03 07*", "01 03 10*"]},
        },
    }
    assert variables == expected


def test_get_gql_variables_with_all_optional_fields():
    waste_codes = ["01 03 05*", "01 03 07*", "01 03 10*"]
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.OUTGOING,
        export_format=RegistryV2Format.XLSX,
        start_date=datetime(2023, 8, 1),
        end_date=datetime(2023, 8, 31),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=True,
        waste_types_dd=True,
        waste_types_texs=False,
        waste_codes=waste_codes,
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.OUTGOING,
        "format": RegistryV2Format.XLSX,
        "dateRange": {"_gte": "2023-08-01T00:00:00", "_lte": "2023-08-31T00:00:00"},
        "where": {
            "declarationType": {"_eq": RegistryV2DeclarationType.ALL},
            "wasteType": {"_in": ["DND", "DD"]},
            "wasteCode": {"_in": ["01 03 05*", "01 03 07*", "01 03 10*"]},
        },
    }
    assert variables == expected


def test_get_gql_variables_with_empty_waste_codes():
    """Test with empty waste codes list."""
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.INCOMING,
        export_format=RegistryV2Format.CSV,
        start_date=datetime(2023, 2, 1),
        end_date=datetime(2023, 2, 28),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=False,
        waste_types_dd=False,
        waste_types_texs=False,
        waste_codes=[],
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.INCOMING,
        "format": RegistryV2Format.CSV,
        "dateRange": {"_gte": "2023-02-01T00:00:00", "_lte": "2023-02-28T00:00:00"},
        "where": {"declarationType": {"_eq": RegistryV2DeclarationType.ALL}},
    }
    assert variables == expected


def test_get_gql_variables_with_waste_types_and_codes():
    """Test with both waste types and waste codes."""
    waste_codes = [
        "01 03 05*",
    ]
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.OUTGOING,
        export_format=RegistryV2Format.CSV,
        start_date=datetime(2023, 9, 15),
        end_date=datetime(2023, 9, 30),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=False,
        waste_types_dd=True,
        waste_types_texs=True,
        waste_codes=waste_codes,
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.OUTGOING,
        "format": RegistryV2Format.CSV,
        "dateRange": {"_gte": "2023-09-15T00:00:00", "_lte": "2023-09-30T00:00:00"},
        "where": {
            "declarationType": {"_eq": RegistryV2DeclarationType.ALL},
            "wasteType": {"_in": ["DD", "TEXS"]},
            "wasteCode": {
                "_in": [
                    "01 03 05*",
                ]
            },
        },
    }
    assert variables == expected


def test_get_gql_variables_only_texs_waste_type():
    export = RegistryV2ExportFactory(
        siret="98765432109876",
        registry_type=RegistryV2ExportType.INCOMING,
        export_format=RegistryV2Format.CSV,
        start_date=datetime(2023, 4, 1),
        end_date=datetime(2023, 4, 15),
        declaration_type=RegistryV2DeclarationType.ALL,
        waste_types_dnd=False,
        waste_types_dd=False,
        waste_types_texs=True,
        waste_codes=[],
    )

    variables = export.get_gql_variables()

    expected = {
        "siret": "98765432109876",
        "registryType": RegistryV2ExportType.INCOMING,
        "format": RegistryV2Format.CSV,
        "dateRange": {"_gte": "2023-04-01T00:00:00", "_lte": "2023-04-15T00:00:00"},
        "where": {"declarationType": {"_eq": RegistryV2DeclarationType.ALL}, "wasteType": {"_in": ["TEXS"]}},
    }
    assert variables == expected
