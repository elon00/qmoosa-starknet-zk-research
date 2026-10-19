"""Starknet Cairo & ZK Verification Engine."""
FIELD_PRIME = 2**251 + 17 * 2**192 + 1

def validate_felt(value: int) -> bool:
    return 0 <= value < FIELD_PRIME

def pedersen_hash_sim(a: int, b: int) -> int:
    import hashlib
    h = hashlib.sha256(f"{a}:{b}".encode()).hexdigest()
    return int(h, 16) % FIELD_PRIME
