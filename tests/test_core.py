import unittest

from infralens import inventory


class InfraLensTests(unittest.TestCase):
    def test_inventory(self):
        self.assertEqual(
            inventory([
                {"type": "server", "name": "web"},
                {"type": "server", "name": "api"},
                {"type": "db", "name": "main"},
                {"type": "server", "name": "web"},
            ]),
            {"db": ["main"], "server": ["api", "web"]},
        )


if __name__ == "__main__":
    unittest.main()
