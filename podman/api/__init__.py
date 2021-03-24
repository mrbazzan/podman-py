"""Tools for connecting to a Podman service."""
from podman.api.client import APIClient
from podman.api.parse_utils import (
    decode_header,
    parse_repository,
    prepare_body,
    prepare_cidr,
    prepare_timestamp,
)
from podman.api.tar_utils import create_tar, prepare_containerfile, prepare_dockerignore
from podman.api.url_utils import prepare_filters

from . import version

DEFAULT_TIMEOUT: float = 60.0
DEFAULT_CHUNK_SIZE = 2 * 1024 * 1024

API_VERSION: str = version.__version__
COMPATIBLE_VERSION: str = version.__compatible_version__

# isort: unique-list
__all__ = [
    'APIClient',
    'API_VERSION',
    'COMPATIBLE_VERSION',
    'DEFAULT_CHUNK_SIZE',
    'DEFAULT_TIMEOUT',
    'create_tar',
    'decode_header',
    'parse_repository',
    'prepare_body',
    'prepare_cidr',
    'prepare_containerfile',
    'prepare_dockerignore',
    'prepare_filters',
    'prepare_timestamp',
]