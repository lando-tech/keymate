"""
Validation logic for key options from the key generation form
"""

import os


def validate_key_size(key_type: str, key_size: int):
    """
    Validate the key size for the given key type
    """
    if key_type == "ed25519" and key_size != 0:
        return False
    if key_type == "rsa":
        return key_size in set(2048, 3072, 4096)
    return False


def validate_key_path(key_path):
    """
    validate key_path
    """
    return os.path.exists(key_path)
