import os
import tempfile
from contextlib import contextmanager
import logging
import threading
from typing import Any, Optional

import sshtunnel
from django.conf import LazySettings

logger = logging.getLogger(__name__)

_tunnel_info: dict[str, Any] = {}
_tunnel_lock = threading.Lock()


def set_tunnel(tunnel: sshtunnel.SSHTunnelForwarder):
    _tunnel_info["tunnel"] = tunnel
    _tunnel_info["port"] = tunnel.local_bind_port


def get_tunnel() -> Optional[sshtunnel.SSHTunnelForwarder]:
    return _tunnel_info.get("tunnel")


def get_tunnel_port() -> Optional[int]:
    return _tunnel_info.get("port")


def is_tunnel_active(tunnel: sshtunnel.SSHTunnelForwarder) -> bool:
    return tunnel.is_active


def ssh_tunnel(settings: LazySettings):
    """
    Maintains a single active SSH tunnel across the application lifetime.
    Reuses the tunnel if already open, and reopens it if necessary.
    """

    with _tunnel_lock:
        tunnel = get_tunnel()

        if tunnel and is_tunnel_active(tunnel):
            # Tunnel is already open and active
            logger.debug("Reusing existing ssh tunnel")
            return tunnel

        logger.info("Creating new ssh tunnel")
        # Otherwise, create a new tunnel
        temp_key_file = tempfile.NamedTemporaryFile(mode="w", delete=False)

        try:
            temp_key_file.write(settings.DWH_SSH_KEY)
            temp_key_file.close()
            os.chmod(temp_key_file.name, 0o600)

            tunnel = sshtunnel.open_tunnel(
                (settings.DWH_SSH_HOST, int(settings.DWH_SSH_PORT)),
                ssh_username=settings.DWH_SSH_USERNAME,
                ssh_pkey=temp_key_file.name,
                remote_bind_address=("localhost", int(settings.DWH_PORT)),
            )

            tunnel.start()
            set_tunnel(tunnel)

            return tunnel
        finally:
            os.unlink(temp_key_file.name)
