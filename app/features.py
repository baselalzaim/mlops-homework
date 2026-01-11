import hashlib

def hash_feature(value: str, num_buckets: int = 100) -> int:
    hash_object = hashlib.md5(value.encode())
    return int(hash_object.hexdigest(), 16) % num_buckets
