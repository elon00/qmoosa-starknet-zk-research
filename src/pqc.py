"""NIST Post-Quantum Cryptography (FIPS 203/204) Harness."""
import hashlib

def ml_kem_encapsulate_sim(public_key: bytes) -> tuple:
    shared_secret = hashlib.sha256(public_key + b":kem_secret").digest()
    ciphertext = hashlib.sha256(public_key + b":kem_cipher").digest()
    return shared_secret, ciphertext

def ml_dsa_verify_sim(message: bytes, signature: bytes, public_key: bytes) -> bool:
    expected = hashlib.sha256(public_key + message).digest()
    return signature == expected
