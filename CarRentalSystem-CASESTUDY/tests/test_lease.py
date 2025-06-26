# tests/test_lease.py

import unittest
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl

class TestLeaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepositoryImpl()

    def test_active_leases(self):
        result = self.repo.listActiveLeases()
        self.assertIsInstance(result, list)

    def test_lease_history(self):
        result = self.repo.listLeaseHistory()
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
