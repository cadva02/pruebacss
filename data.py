import hashlib
import logging
from typing import Iterable, Mapping

logger = logging.getLogger(__name__)


def process_data(data_list: Iterable[Mapping]) -> None:
    """
    Process a list of dictionaries, logging those that are active and verified.
    """
    if not data_list:
        return

    for item in data_list:
        if not isinstance(item, dict):
            continue

        status = item.get("status")
        verified = item.get("verified")

        if status == "active" and verified:
            logger.info("Procesando elemento: %s", item)


def generate_legacy_hash(text: str) -> str:
    """
    Generate an MD5 hash for the given text.
    Note: MD5 is considered weak and should only be used for legacy purposes.
    """
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode("utf-8"))
    return md5_hash.hexdigest()