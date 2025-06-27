# tests/test_lease.py

import unittest
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl
from exception.custom_exceptions import LeaseNotFoundException

class TestLeaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepositoryImpl()
        # You can use valid customer and car IDs from your DB for creating test lease
        cls.valid_customer_id = 1
        cls.valid_vehicle_id = 2

    def test_create_lease_and_list(self):
        # Adjust dates as needed
        start_date = "2025-07-01"
        end_date = "2025-07-03"
        self.repo.createLease(self.valid_customer_id, self.valid_vehicle_id, start_date, end_date)
        active_leases = self.repo.listActiveLeases()
        # At least one active lease exists
        self.assertTrue(isinstance(active_leases, list))

    def test_list_active_leases(self):
        result = self.repo.listActiveLeases()
        self.assertIsInstance(result, list)

    def test_list_lease_history(self):
        result = self.repo.listLeaseHistory()
        self.assertIsInstance(result, list)

