import datetime as dt
from functools import reduce
from typing import List, TypedDict

from .constants import (
    BSDASRI_HUMAN_WASTE_CODE,
    ES_TYPE_BSDA,
    ES_TYPE_BSDASRI,
    ES_TYPE_BSDD,
    ES_TYPE_BSFF,
    ES_TYPE_BSPAOH,
    TYPE_BPAOH,
    TYPE_BSDA,
    TYPE_BSDASRI,
    TYPE_BSDD,
    TYPE_BSFF,
)


class WasteDetails(TypedDict):
    code: str
    name: str
    weight: str


class Company(TypedDict):
    name: str


class Actor(TypedDict):
    company: Company


class BsdDisplay(TypedDict):
    bsd_type: str
    id: str
    readable_id: str
    updated_at: str
    adr: str
    waste_details: WasteDetails
    emitter: Actor
    destination: Actor
    transporter: Actor
    transporter_plate: str
    packagings: str


def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)


def format_date(str):
    if not str:
        return ""
    try:
        return dt.datetime.fromisoformat(str).strftime("%d/%m/%Y")
    except ValueError:
        return ""


def format_bsdd_packagings(packagings):
    if not packagings:
        return ""
    return ", ".join([f"{p.get('quantity')} {p.get('other') or p.get('type')}" for p in packagings])


def format_bsdasri_packagings(packagings):
    if not packagings:
        return ""
    return ", ".join([f"{p.get('quantity')} {p.get('other') or p.get('type')}" for p in packagings])


def format_bsff_packagings(packagings):
    if not packagings:
        return ""
    return ", ".join(
        [f"{p.get('numero')} {p.get('type')} vol:{p.get('volume')} poids:{p.get('weight')}" for p in packagings]
    )


def format_bspaoh_packagings(packagings):
    if not packagings:
        return ""
    return ", ".join([f"{p.get('quantity')} {p.get('type')} vol:{p.get('volume')}" for p in packagings])


# BsdDisplay = TypedDict('BsdDisplay', {'bsd_type': str, 'id': str, "readable_id": str, "updated_at": str, "adr": str})


def bsdd_to_bsd_display(bsdd) -> BsdDisplay:
    return {
        "bsd_type": TYPE_BSDD,
        "id": deep_get(bsdd, "id"),
        "readable_id": deep_get(bsdd, "readableId", None) or deep_get(bsdd, "id"),
        "updated_at": format_date(deep_get(bsdd, "updatedAt")),
        "adr": deep_get(bsdd, "wasteDetails.onuCode"),
        "waste_details": {
            "code": deep_get(bsdd, "wasteDetails.code"),
            "name": deep_get(bsdd, "wasteDetails.name"),
            "weight": str(deep_get(bsdd, "stateSummary.quantity") or deep_get(bsdd, "wasteDetails.quantity")),
            # force str to get a dot an not a comma,
        },
        "emitter": {"company": {"name": deep_get(bsdd, "emitter.company.name")}},
        "destination": {"company": {"name": deep_get(bsdd, "recipient.company.name")}},
        "transporter": {
            "company": {
                "name": deep_get(bsdd, "transporter.company.name"),
                "siret": deep_get(bsdd, "transporter.company.siret"),
            }
        },
        "transporter_plate": deep_get(bsdd, "transporter.numberPlate")
        or deep_get(bsdd, "stateSummary.transporterNumberPlate"),
        "packagings": format_bsdd_packagings(deep_get(bsdd, "wasteDetails.packagingInfos")),
    }


def bsff_to_bsd_display(bsff) -> BsdDisplay:
    return {
        "bsd_type": TYPE_BSFF,
        "id": deep_get(bsff, "id"),
        "readable_id": deep_get(bsff, "id"),
        "updated_at": format_date(deep_get(bsff, "bsffUpdatedAt")),
        "adr": deep_get(bsff, "waste.adr"),
        "waste_details": {
            "code": deep_get(bsff, "waste.code"),
            "name": deep_get(bsff, "waste.description"),
            "weight": str(deep_get(bsff, "bsffWeight.value")),
            # force str to get a dot an not a comma,
        },
        "emitter": {"company": {"name": deep_get(bsff, "emitter.company.name")}},
        "destination": {"company": {"name": deep_get(bsff, "bsffDestination.company.name")}},
        "transporter": {
            "company": {
                "name": deep_get(bsff, "bsffTransporter.company.name"),
                "siret": deep_get(bsff, "bsffTransporter.company.siret"),
            }
        },
        "transporter_plate": ",".join(deep_get(bsff, "bsffTransporter.transport.plates")),
        "packagings": format_bsff_packagings(deep_get(bsff, "packagings")),
    }


def bsdasri_to_bsd_display(bsdasri) -> BsdDisplay:
    waste_code = deep_get(bsdasri, "bsdasriWaste.code")

    return {
        "bsd_type": TYPE_BSDASRI,
        "id": deep_get(bsdasri, "id"),
        "readable_id": deep_get(bsdasri, "id"),
        "updated_at": format_date(deep_get(bsdasri, "updatedAt")),
        "adr": deep_get(bsdasri, "bsdasriWaste.adr"),
        "waste_details": {
            "code": waste_code,
            "name": "DASRI origine humaine" if waste_code == BSDASRI_HUMAN_WASTE_CODE else "DASRI origine animale",
            "weight": str(deep_get(bsdasri, "transporter.transport.weight.value", default=0)),
            # force str to get a dot an not a comma
        },
        "emitter": {"company": {"name": deep_get(bsdasri, "emitter.company.name")}},
        "destination": {"company": {"name": deep_get(bsdasri, "destination.company.name")}},
        "transporter": {
            "company": {
                "name": deep_get(bsdasri, "transporter.company.name"),
                "siret": deep_get(bsdasri, "transporter.company.siret"),
            }
        },
        "transporter_plate": ",".join(
            deep_get(bsdasri, "transporter.transport.plates", default=[])
            or deep_get(bsdasri, "bsdasriTransporter.transport.plates", default=[])
        ),
        "packagings": format_bsdasri_packagings(deep_get(bsdasri, "transporter.transport.packagings", default=[])),
    }


def bsda_to_bsd_display(bsda) -> BsdDisplay:
    waste_code = deep_get(bsda, "waste.bsdaWasteCode")

    return {
        "bsd_type": TYPE_BSDA,
        "id": deep_get(bsda, "id"),
        "readable_id": deep_get(bsda, "id"),
        "updated_at": format_date(deep_get(bsda, "updatedAt")),
        "adr": deep_get(bsda, "waste.adr"),
        "waste_details": {
            "code": waste_code,
            "name": deep_get(bsda, "waste.materialName"),
            "weight": str(deep_get(bsda, "weight.value", default=0)),
            # force str to get a dot an not a comma
        },
        "emitter": {"company": {"name": deep_get(bsda, "emitter.company.name")}},
        "destination": {"company": {"name": deep_get(bsda, "destination.company.name")}},
        "transporter": {
            "company": {
                "name": deep_get(bsda, "transporter.company.name"),
                "siret": deep_get(bsda, "transporter.company.siret"),
            }
        },
        "transporter_plate": ",".join(deep_get(bsda, "transporter.transport.plates", default=[])),
        "packagings": format_bsdasri_packagings(deep_get(bsda, "transporter.transport.packagings", default=[])),
    }


def bspaoh_to_bsd_display(bspaoh) -> BsdDisplay:
    waste_code = deep_get(bspaoh, "bspaohWaste.code")
    waste_type = deep_get(bspaoh, "bspaohWaste.type")

    return {
        "bsd_type": TYPE_BPAOH,
        "id": deep_get(bspaoh, "id"),
        "readable_id": deep_get(bspaoh, "id"),
        "updated_at": format_date(deep_get(bspaoh, "updatedAt")),
        "adr": "Non applicable",
        "waste_details": {
            "code": waste_code,
            "name": "Foetus" if waste_type == "FOETUS" else "Pièces anatomiques d'origine humainee",
            "weight": str(deep_get(bspaoh, "emitter.emission.detail.weight.value", default=0)),
            # force str to get a dot an not a comma
        },
        "emitter": {"company": {"name": deep_get(bspaoh, "emitter.company.name")}},
        "destination": {"company": {"name": deep_get(bspaoh, "destination.company.name")}},
        "transporter": {
            "company": {
                "name": deep_get(bspaoh, "transporter.company.name"),
                "siret": deep_get(bspaoh, "transporter.company.siret"),
            }
        },
        "transporter_plate": ",".join(
            deep_get(bspaoh, "transporter.transport.plates", default=[])
            or deep_get(bspaoh, "bsdasriTransporter.transport.plates", default=[])
        ),
        "packagings": format_bspaoh_packagings(deep_get(bspaoh, "bspaohWaste.packagings", default=[])),
    }


class BsdsToBsdsDisplay:
    def __init__(self, bsds):
        self.bsds: List[BsdDisplay] = bsds
        self.bsds_display = []

    def map_bsd_to_bsd_display(self, bsd):
        converters = {
            ES_TYPE_BSDD: bsdd_to_bsd_display,
            ES_TYPE_BSDASRI: bsdasri_to_bsd_display,
            ES_TYPE_BSFF: bsff_to_bsd_display,
            ES_TYPE_BSDA: bsda_to_bsd_display,
            ES_TYPE_BSPAOH: bspaoh_to_bsd_display,
        }

        bsd_type = bsd["__typename"]
        converter = converters.get(bsd_type)
        if converter:
            return converter(bsd)

        return None

    def convert(self):
        for bsd in self.bsds:
            bsd_display = self.map_bsd_to_bsd_display(bsd)
            if bsd_display:
                self.bsds_display.append(bsd_display)
