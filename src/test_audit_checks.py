import unittest
from audit_checks import run_all

class AuditChecksTest(unittest.TestCase):
    def test_all_checks_return_non_negative_counts(self):
        results = run_all()
        self.assertTrue(results)
        for count in results.values():
            self.assertGreaterEqual(count, 0)

if __name__ == "__main__":
    unittest.main()
