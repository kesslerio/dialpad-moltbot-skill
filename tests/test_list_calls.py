from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from list_calls import CALLS_ENDPOINT, normalize_duration


class ListCallsTests(unittest.TestCase):
    def test_calls_endpoint_uses_singular_path(self):
        self.assertTrue(CALLS_ENDPOINT.endswith("/api/v2/call"))

    def test_normalize_duration_treats_values_as_milliseconds(self):
        self.assertEqual(normalize_duration({"duration": 5000}), 5)
        self.assertEqual(normalize_duration({"duration": 120000}), 120)
        self.assertEqual(normalize_duration({"total_duration": 9000}), 9)


if __name__ == "__main__":
    unittest.main()
