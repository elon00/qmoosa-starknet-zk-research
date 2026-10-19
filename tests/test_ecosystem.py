import unittest
from src.adapter import *
from src.quicknode import QuickNodeClient
from src.x402 import generate_payment_required_header
from src.pqc import ml_kem_encapsulate_sim, ml_dsa_verify_sim
from src.rsi_rea import governed_rsi_cycle

class AdvancedEcosystemTests(unittest.TestCase):
    def test_quicknode_health(self):
        qn = QuickNodeClient()
        self.assertEqual(qn.check_health()["status"], "HEALTHY")

    def test_x402_header(self):
        hdr = generate_payment_required_header("agent-compute", 0.05)
        self.assertEqual(hdr["status"], 402)
        self.assertEqual(hdr["x402-price-usd"], "0.05")

    def test_pqc_simulation(self):
        pk = b"test_pqc_public_key_32_bytes_sample"
        secret, cipher = ml_kem_encapsulate_sim(pk)
        self.assertEqual(len(secret), 32)
        self.assertEqual(len(cipher), 32)

    def test_rsi_governance(self):
        result = governed_rsi_cycle(0.85, 0.92)
        self.assertEqual(result["status"], "APPROVED")
        regressed = governed_rsi_cycle(0.85, 0.81)
        self.assertEqual(regressed["status"], "REJECTED_REGRESSION")

if __name__ == "__main__":
    unittest.main()
