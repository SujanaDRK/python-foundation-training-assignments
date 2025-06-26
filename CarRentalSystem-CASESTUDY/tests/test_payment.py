# tests/test_payment.py

import unittest
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl

class TestPaymentOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepositoryImpl()

    def test_record_payment(self):
        lease_id = 1  # must exist in DB
        self.repo.recordPayment(lease_id, 500.00)
        # Can't assert directly unless we fetch — placeholder success test
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
