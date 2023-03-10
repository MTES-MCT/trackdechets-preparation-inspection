from typing import Any, Union

import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from .queries import (
    sql_bsda_query_str,
    sql_bsdasri_query_str,
    sql_bsdd_query_str,
    sql_bsff_query_str,
    sql_bsvhu_query_str,
    sql_company_query_str,
    sql_get_broker_receipt_id_data,
    sql_get_icpe_data,
    sql_get_trader_receipt_id_data,
    sql_get_transporter_receipt_id_data_str,
    sql_get_vhu_agrement_data,
    sql_revised_bsda_query_str,
    sql_revised_bsdd_query_str,
)

wh_engine = create_engine(settings.WAREHOUSE_URL)

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
    date_params = None
    if date_columns is not None:
        date_params = {e: {"utc": True} for e in date_columns}
    # todo: use utc
    engine = create_engine(settings.WAREHOUSE_URL)
    df = pd.read_sql_query(
        query,
        params=query_params,
        con=engine,
        dtype=dtypes,
        parse_dates=date_columns,
    )

    return df


def build_bsdd_query(siret, date_params=None):
    df = build_query(
        sql_bsdd_query_str,
        query_params={"siret": siret},
        date_columns=bsd_date_params,
        dtypes=bs_dtypes,
    )

    return df


def build_bsda_query(siret, date_params=None):
    date_params = ["sent_at", "received_at", "processed_at"]
    return build_query(
        sql_bsda_query_str,
        query_params={"siret": siret},
        date_columns=bsd_date_params,
    )


def build_bsdasri_query(siret, date_params=None):
    date_params = ["sent_at", "received_at", "processed_at"]
    return build_query(
        sql_bsdasri_query_str,
        query_params={"siret": siret},
        date_columns=bsd_date_params,
    )


def build_bsff_query(siret, date_params=None):
    date_params = ["sent_at", "received_at", "processed_at"]
    return build_query(
        sql_bsff_query_str,
        query_params={"siret": siret},
        date_columns=bsd_date_params,
    )


def build_bsvhu_query(siret, date_params=None):
    date_params = ["sent_at", "received_at", "processed_at"]
    return build_query(sql_bsvhu_query_str, query_params={"siret": siret})


def build_query_company(siret, date_params=None):
    return build_query(
        sql_company_query_str,
        query_params={"siret": siret},
        date_columns=date_params,
    )


company_query_config = [
    {
        "name": "transporter_receipt",
        "column": "transporter_receipt_id",
        "sql": sql_get_transporter_receipt_id_data_str,
    },
    {
        "name": "trader_receipt",
        "column": "trader_receipt_id",
        "sql": sql_get_trader_receipt_id_data,
    },
    {
        "name": "broker_receip",
        "column": "broker_receipt_id",
        "sql": sql_get_broker_receipt_id_data,
    },
    {
        "name": "vhu_agrement_demolisseur",
        "column": "vhu_agrement_demolisseur_id",
        "sql": sql_get_vhu_agrement_data,
    },
    {
        "name": "vhu_agrement_broyeu",
        "column": "vhu_agrement_broyeur_id",
        "sql": sql_get_vhu_agrement_data,
    },
]


def get_agreement_data(company_data_df: pd.DataFrame) -> dict:
    res = {}
    for config in company_query_config:
        id_ = company_data_df[config["column"]].item()
        if id_ is not None:
            df = build_query(
                config["sql"],
                date_columns=["validity_limit"],
                query_params={"id": id_},
            )
            if len(df) != 0:
                res[config["name"]] = df.to_json()
    return res


def get_icpe_data(siret: str) -> Union[pd.DataFrame, None]:
    icpe_data = build_query(
        sql_get_icpe_data,
        query_params={"siret": siret},
        date_columns=["date_debut_exploitation", "date_fin_validite"],
    )

    if len(icpe_data):
        return icpe_data
    return None
