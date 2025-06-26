# tests/test_customer.py

import unittest
from entity.customer import Customer
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl

class TestCustomerOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepositoryImpl()
        cls.test_customer = Customer(0, "Test", "User", "test.user@example.com", "9998887777")

    def test_add_customer(self):
        self.repo.addCustomer(self.test_customer)
        customers = self.repo.listCustomers()
        self.assertTrue(any(c[2] == "User" for c in customers))

    def test_find_customer(self):
        result = self.repo.findCustomerById(1)
        self.assertIsNotNone(result)

    def test_list_customers(self):
        customers = self.repo.listCustomers()
        self.assertIsInstance(customers, list)

if __name__ == "__main__":
    unittest.main()
