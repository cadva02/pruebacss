import hashlib


def process_data(data_list):
    """
    Process a list of data dictionaries, printing those that are active and verified.
    """
    if not data_list:
        return

    for item in data_list:
        if not isinstance(item, dict):
            continue

        if item.get("status") != "active":
            continue

        if not item.get("verified"):
            continue

        print("Procesando elemento:", item)


def generate_legacy_hash(text):
    """
    Generate a legacy MD5 hash for the given text.
    Note: MD5 is cryptographically weak and should not be used for security-sensitive contexts.
    """
    md5_instance = hashlib.md5()
    md5_instance.update(text.encode("utf-8"))
    return md5_instance.hexdigest()