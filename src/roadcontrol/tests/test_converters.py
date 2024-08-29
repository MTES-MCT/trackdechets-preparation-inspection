from ..converters import (
    bsda_to_bsd_display,
    bsdasri_to_bsd_display,
    bsdd_to_bsd_display,
    bsff_to_bsd_display,
    bspaoh_to_bsd_display,
)


def test_bsdd_to_bsd_display():
    es_bsdd = {
        "__typename": "Form",
        "bsddStatus": "SENT",
        "emitter": {"company": {"name": "DECHETTERIE DE LA BAS "}, "workSite": None},
        "id": "xyz123",
        "readableId": "BSD-1238-ABCD",
        "recipient": {"company": {"name": "THE COMPANY "}},
        "stateSummary": {"quantity": 0.02},
        "transporter": {"company": {"name": "THE COMPANY "}, "numberPlate": "FN605TG"},
        "transporters": [{"company": {"name": "THE COMPANY "}, "numberPlate": "XY605TG"}],
        "updatedAt": "2024-11-15T09:43:13.790Z",
        "wasteDetails": {
            "code": "15 02 02*",
            "name": " Materiaux souilles",
            "onuCode": "UN 3175 DECHET SOLIDES CONTENANT DU LIQUIDE",
            "packagingInfos": [
                {"other": "Caisse croco", "quantity": 1, "type": "AUTRE"},
                {"other": "synchro", "quantity": 1, "type": "AUTRE"},
            ],
            "quantity": 0.02,
        },
    }
    bsd_display = bsdd_to_bsd_display(es_bsdd)
    assert bsd_display == {
        "bsd_type": "BSDD",
        "adr": "UN 3175 DECHET SOLIDES CONTENANT DU LIQUIDE",
        "destination": {"company": {"name": "THE COMPANY "}},
        "emitter": {"company": {"name": "DECHETTERIE DE LA BAS "}},
        "id": "xyz123",
        "packagings": "1 Caisse croco, 1 synchro",
        "readable_id": "BSD-1238-ABCD",
        "transporter": {"company": {"name": "THE COMPANY "}},
        "transporter_plate": "FN605TG",
        "waste_details": {"code": "15 02 02*", "name": " Materiaux souilles", "weight": "0.02"},
        "updated_at": "15/11/2024",
    }


def test_bsdasri_to_bsd_display():
    es_bsdasri = {
        "__typename": "Bsdasri",
        "bsdasriStatus": "SENT",
        "bsdasriWaste": {
            "adr": "UN , DECHET, Quantité estimée conformément au " "5.4.1.1.3.2",
            "code": "18 01 03*",
        },
        "destination": {"company": {"name": "DESTI"}},
        "emitter": {"company": {"name": "EMITTER"}},
        "id": "DASRI-123_XYY",
        "transporter": {
            "company": {"name": "THE COMPANY"},
            "transport": {"plates": ["DQ-199-NS"], "weight": {"value": 12}},
        },
        "updatedAt": "2024-11-15T09:43:13.790Z",
    }
    bsd_display = bsdasri_to_bsd_display(es_bsdasri)
    assert bsd_display == {
        "bsd_type": "BSDASRI",
        "adr": "UN , DECHET, Quantité estimée conformément au 5.4.1.1.3.2",
        "destination": {"company": {"name": "DESTI"}},
        "emitter": {"company": {"name": "EMITTER"}},
        "id": "DASRI-123_XYY",
        "packagings": "",
        "readable_id": "DASRI-123_XYY",
        "transporter": {"company": {"name": "THE COMPANY"}},
        "transporter_plate": "DQ-199-NS",
        "updated_at": "15/11/2024",
        "waste_details": {"code": "18 01 03*", "name": "DASRI origine humaine", "weight": "12"},
    }


def test_bsff_to_bsd_display():
    es_bsff = {
        "__typename": "Bsff",
        "bsffUpdatedAt": "2024-11-15T09:43:13.790Z",
        "bsffDestination": {"company": {"name": "THE COMPANY"}},
        "bsffStatus": "SENT",
        "bsffTransporter": {"company": {"name": "THE COMPANY", "siret": "123"}, "transport": {"plates": ["FR-SD-FR"]}},
        "bsffWeight": {"value": 1},
        "emitter": {"company": {"name": "THE COMPANY"}},
        "id": "FF-123-XY",
        "packagings": [{"numero": "2222222", "type": "BOUTEILLE", "volume": 12.5, "weight": 1}],
        "waste": {"code": "14 06 01*", "description": "R-410A", "adr": "lorem ipsum"},
    }

    bsd_display = bsff_to_bsd_display(es_bsff)

    assert bsd_display == {
        "bsd_type": "BSFF",
        "adr": "lorem ipsum",
        "destination": {
            "company": {
                "name": "THE COMPANY",
            }
        },
        "emitter": {"company": {"name": "THE COMPANY"}},
        "id": "FF-123-XY",
        "readable_id": "FF-123-XY",
        "packagings": "2222222 BOUTEILLE vol:12.5 poids:1",
        "transporter": {"company": {"name": "THE COMPANY"}},
        "transporter_plate": "FR-SD-FR",
        "updated_at": "15/11/2024",
        "waste_details": {"code": "14 06 01*", "name": "R-410A", "weight": "1"},
    }


def test_bsda_to_bsd_display():
    es_bsda = {
        "__typename": "Bsda",
        "bsdaPackagings": [
            {"other": "", "quantity": 2, "type": "DEPOT_BAG"},
            {"other": "", "quantity": 1, "type": "CONTENEUR_BAG"},
            {"other": "", "quantity": 1, "type": "BIG_BAG"},
        ],
        "bsdaStatus": "SENT",
        "destination": {"company": {"name": "THE COMPANY"}},
        "emitter": {"company": {"name": "EMITTER"}},
        "id": "BSDA-123-XYZ",
        "transporter": {"company": {"name": "TRANSPORT"}, "transport": {"plates": ["34ER36"]}},
        "waste": {"adr": "non sousmis", "bsdaWasteCode": "17 06 05*", "materialName": "amiante ciment lié"},
        "weight": {"value": 10.1},
    }

    bsd_display = bsda_to_bsd_display(es_bsda)

    assert bsd_display == {
        "bsd_type": "BSDA",
        "id": "BSDA-123-XYZ",
        "readable_id": "BSDA-123-XYZ",
        "updated_at": "",
        "adr": "non sousmis",
        "waste_details": {"code": "17 06 05*", "name": "amiante ciment lié", "weight": "10.1"},
        "emitter": {"company": {"name": "EMITTER"}},
        "destination": {"company": {"name": "THE COMPANY"}},
        "transporter": {"company": {"name": "TRANSPORT"}},
        "transporter_plate": "34ER36",
        "packagings": "",
    }


def test_bspaoh_to_bsd_display():
    es_bpaoh = {
        "__typename": "Bspaoh",
        "bspaohStatus": "SENT",
        "bspaohWaste": {
            "code": "18 01 02",
            "packagings": [{"quantity": 1, "type": "BIG_BOX", "volume": 1}],
            "type": "PAOH",
        },
        "destination": {"company": {"name": "Établissement de test"}},
        "emitter": {"company": {"name": "Établissement de test"}, "emission": {"detail": {"weight": {"value": 10}}}},
        "id": "PAOH-20240826-ZCF7DH7V1",
        "transporter": {"company": {"name": "Établissement de test"}, "transport": {"plates": ["az-ta-87"]}},
    }

    bsd_display = bspaoh_to_bsd_display(es_bpaoh)

    assert bsd_display == {
        "bsd_type": "BSPAOH",
        "id": "PAOH-20240826-ZCF7DH7V1",
        "readable_id": "PAOH-20240826-ZCF7DH7V1",
        "updated_at": "",
        "adr": "Non applicable",
        "waste_details": {"code": "18 01 02", "name": "Pièces anatomiques d'origine humainee", "weight": "10"},
        "emitter": {"company": {"name": "Établissement de test"}},
        "destination": {"company": {"name": "Établissement de test"}},
        "transporter": {"company": {"name": "Établissement de test"}},
        "transporter_plate": "az-ta-87",
        "packagings": "1 BIG_BOX vol:1",
    }
