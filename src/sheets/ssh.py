import tempfile
import os
import sshtunnel
from contextlib import contextmanager


@contextmanager
def ssh_tunnel(settings):
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
            local_bind_address=(settings.DWH_SSH_LOCAL_BIND_HOST, int(settings.DWH_SSH_LOCAL_BIND_PORT)),
        )

        tunnel.start()
        yield tunnel
    finally:
        tunnel.stop()
        os.unlink(temp_key_file.name)
