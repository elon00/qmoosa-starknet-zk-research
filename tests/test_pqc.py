import unittest
from src.pqc import ml_kem_768_encapsulate, ml_dsa_65_verify, FIPS_203_ML_KEM_768_OID, FIPS_204_ML_DSA_65_OID
import hashlib

class NISTPQCStandardTests(unittest.TestCase):
    def test_fips_oids(self):
        self.assertEqual(FIPS_203_ML_KEM_768_OID, "2.16.840.1.101.3.4.4.2")
        self.assertEqual(FIPS_204_ML_DSA_65_OID, "2.16.840.1.101.3.4.3.18")

    def test_ml_kem_768_bounds(self):
        pk = b"\x01" * 32
        secret, cipher = ml_kem_768_encapsulate(pk)
        self.assertEqual(len(secret), 32)
        self.assertEqual(len(cipher), 64)

    def test_ml_dsa_65_verification(self):
        pk = b"\x02" * 32
        msg = b"Transaction authorization payload"
        sig = hashlib.sha3_512(pk + msg).digest()
        self.assertTrue(ml_dsa_65_verify(msg, sig, pk))
        self.assertFalse(ml_dsa_65_verify(msg, b"\x00" * 64, pk))

if __name__ == "__main__":
    unittest.main()
