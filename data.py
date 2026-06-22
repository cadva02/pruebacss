import hashlib
import logging
from typing import Iterable, Mapping, Any, List, Dict

logger = logging.getLogger(__name__)


def process_data(data_list: Iterable[Mapping[str, Any]] | None) -> None:
    """
    Process a list of dictionaries containing status and verification data.

    Only items that:
    - are mappings/dicts
    - have status == "active"
    - have verified truthy
    will be processed.
    """
    if not data_list:
        return

    for item in data_list:
        if not isinstance(item, Mapping):
            continue

        status = item.get("status")
        if status != "active":
            continue

        if not item.get("verified"):
            continue

        logger.info("Procesando elemento: %s", item)


def generate_legacy_hash(text: str) -> str:
    """
    Generate an MD5 hash for backward compatibility purposes.

    Note: MD5 is considered cryptographically weak and should not be used
    for security-critical operations. Prefer stronger algorithms such as
    SHA-256 when possible.
    """
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode("utf-8"))
    return md5_hash.hexdigest()