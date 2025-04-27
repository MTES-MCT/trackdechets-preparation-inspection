from typing import Any, Optional
import logging

from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection

from django.conf import settings

from sheets.ssh import get_tunnel_port, ssh_tunnel

logger = logging.getLogger(__name__)

_dwh_info: dict[str, Any] = {}


def set_engine(dwh_engine: MockConnection, port: int):
    _dwh_info["engine"] = dwh_engine
    _dwh_info["port"] = port


def get_engine() -> Optional[MockConnection]:
    return _dwh_info.get("engine")


def get_engine_port() -> Optional[int]:
    return _dwh_info.get("port")


def get_wh_sqlachemy_engine(dwh_username: str, dwh_password: str, dwh_ssh_local_bind_host: str) -> MockConnection:
    ssh_tunnel(settings)

    tunnel_port = get_tunnel_port()

    if (get_engine() is None) or (get_engine_port() != tunnel_port):
        logger.info("Creating new engine for datawarehouse.")
        warehouse_url = f"clickhouse+native://{dwh_username}:{dwh_password}@{dwh_ssh_local_bind_host}:{tunnel_port}"
        wh_engine = create_engine(warehouse_url)
        set_engine(wh_engine, tunnel_port)

    return get_engine()
