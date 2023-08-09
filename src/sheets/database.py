from datetime import datetime
from typing import Any, Union

import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from .queries import (
    sql_bsda_query_str,
    sql_bsdasri_query_str,
    sql_bsdd_non_dangerous_query_str,
    sql_bsdd_query_str,
    sql_bsff_packagings_query_str,
    sql_bsff_query_str,
    sql_bsvhu_query_str,
    sql_company_query_str,
    sql_get_broker_receipt_id_data,
    sql_get_icpe_2770_data,
    sql_get_icpe_data,
    sql_get_trader_receipt_id_data,
    sql_get_transporter_receipt_id_data_str,
    sql_get_vhu_agrement_data,
    sql_revised_bsda_query_str,
    sql_revised_bsdd_query_str,
)

wh_engine = create_engine(settings.WAREHOUSE_URL, pool_pre_ping=True)

bsd_date_params = ["created_at", "sent_at", "received_at", "processed_at"]
bs_dtypes = {
    "id": str,
    "created_at": str,
    "sent_at": str,
    "received_at": str,
    "processed_at": str,
    "emitter_company_siret": str,
    "emitter_company_address": str,
    "recipient_company_siret": str,
    "waste_details_quantity": float,
    "quantity_received": float,
    "waste_code": str,
    "status": str,
}


def build_query(
    query_str,
    query_params: dict[str, Any] = None,
    date_columns=None,
    dtypes: dict[str, Any] = None,
):
    query = text(query_str)

    # todo: use utc
    engine = wh_engine
    df = pd.read_sql_query(
        query,
        params=query_params,
        con=engine,
        dtype=dtypes,
        parse_dates=date_columns,
    )

    return df


def build_bsdd_query(
    siret: str, data_start_date: datetime, data_end_date: datetime
) -> pd.DataFrame:
    df = build_query(
        sql_bsdd_query_str,
        query_params={
            "siret": siret,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
        dtypes=bs_dtypes,
    )

    return df


def build_bsdd_non_dangerous_query(
    siret: str, data_start_date: datetime, data_end_date: datetime
) -> pd.DataFrame:
    df = build_query(
        sql_bsdd_non_dangerous_query_str,
        query_params={
            "siret": siret,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
        dtypes=bs_dtypes,
    )

    return df


def build_revised_bsdd_query(
    company_id: str, data_start_date: datetime, data_end_date: datetime
):
    df = build_query(
        sql_revised_bsdd_query_str,
        query_params={
            "company_id": company_id,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
    )

    return df


def build_bsda_query(
    siret: str, data_start_date: datetime, data_end_date: datetime
) -> pd.DataFrame:
    return build_query(
        sql_bsda_query_str,
        query_params={
            "siret": siret,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
    )


def build_revised_bsda_query(
    company_id: str, data_start_date: datetime, data_end_date: datetime
):
    df = build_query(
        sql_revised_bsda_query_str,
        query_params={
            "company_id": company_id,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
    )

    return df


def build_bsdasri_query(
    siret: str, data_start_date: datetime, data_end_date: datetime
) -> pd.DataFrame:
    return build_query(
        sql_bsdasri_query_str,
        query_params={
            "siret": siret,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
    )


def build_bsff_query(
    siret: str, data_start_date: datetime, data_end_date: datetime
) -> pd.DataFrame:
    return build_query(
        sql_bsff_query_str,
        query_params={
            "siret": siret,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
    )


def build_bsff_packagings_query(
    siret: str, data_start_date: datetime, data_end_date: datetime
) -> pd.DataFrame:
    return build_query(
        sql_bsff_packagings_query_str,
        query_params={
            "siret": siret,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=["operation_date", "acceptation_date"],
    )


def build_bsvhu_query(
    siret: str, data_start_date: datetime, data_end_date: datetime
) -> pd.DataFrame:
    return build_query(
        sql_bsvhu_query_str,
        query_params={
            "siret": siret,
            "data_start_date": data_start_date,
            "data_end_date": data_end_date,
        },
        date_columns=bsd_date_params,
    )


def build_query_company(siret, date_params=None):
    return build_query(
        sql_company_query_str,
        query_params={
            "siret": siret,
        },
        date_columns=date_params,
    )


company_query_config = [
    {
        "name": "Récépissé Transporteur",
        "column": "transporter_receipt_id",
        "sql": sql_get_transporter_receipt_id_data_str,
    },
    {
        "name": "Récépissé Négociant",
        "column": "trader_receipt_id",
        "sql": sql_get_trader_receipt_id_data,
    },
    {
        "name": "Récépissé Courtier",
        "column": "broker_receipt_id",
        "sql": sql_get_broker_receipt_id_data,
    },
    {
        "name": "Agrément Démolisseur ",
        "column": "vhu_agrement_demolisseur_id",
        "sql": sql_get_vhu_agrement_data,
    },
    {
        "name": "Agrément Broyeur",
        "column": "vhu_agrement_broyeur_id",
        "sql": sql_get_vhu_agrement_data,
    },
]


def get_agreement_data(company_data_df: pd.DataFrame) -> dict:
    res = {}

    for config in company_query_config:
        try:
            id_ = company_data_df[config["column"]].item()
        except ValueError:
            id_ = None

        if id_ is not None:
            df = build_query(
                config["sql"],
                date_columns=["validity_limit"],
                query_params={"id": id_},
            )
            if len(df) != 0:
                res[config["name"]] = df
    return res


def get_icpe_data(siret: str) -> Union[pd.DataFrame, None]:
    icpe_data = build_query(
        sql_get_icpe_data,
        query_params={
            "siret": siret,
        },
    )

    if len(icpe_data):
        return icpe_data
    return None


def get_icpe_2770_data(siret: str) -> Union[pd.DataFrame, None]:
    icpe_data = build_query(
        sql_get_icpe_2770_data,
        query_params={
            "siret": siret,
        },
    )

    if len(icpe_data):
        return icpe_data
    return None
