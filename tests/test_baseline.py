import unittest
from src.engine import conway_step, state_hash, emission_limit

class RealityBaselineTests(unittest.TestCase):
    def test_still_life(self):
        square = {(0, 0), (0, 1), (1, 0), (1, 1)}
        self.assertEqual(conway_step(square), square)
    def test_blinker(self):
        initial = {(0, 0), (1, 0), (2, 0)}
        self.assertEqual(conway_step(initial), {(1, -1), (1, 0), (1, 1)})
        self.assertEqual(conway_step(conway_step(initial)), initial)
    def test_hash_determinism(self):
        self.assertEqual(state_hash({(2, 1), (0, 0)}), state_hash({(0, 0), (2, 1)}))
    def test_emission_limit(self):
        self.assertEqual(emission_limit(10000, 300, 500), 300)

if __name__ == "__main__":
    unittest.main()
