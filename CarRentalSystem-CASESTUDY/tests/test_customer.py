# tests/test_customer.py
import unittest
from entity.customer import Customer
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl
from exception.custom_exceptions import CustomerNotFoundException

class TestCustomerOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepositoryImpl()
        cls.test_customer = Customer(0, "Temp", "Test", "temp.test@example.com", "8888888888")

    def test_add_and_remove_customer(self):
        # Add
        self.repo.addCustomer(self.test_customer)
        customers = self.repo.listCustomers()
        new_customer = [c for c in customers if c[2] == "Test"]
        self.assertTrue(new_customer)
        new_customer_id = new_customer[0][0]
        # Remove
        self.repo.removeCustomer(new_customer_id)
        customers_after = self.repo.listCustomers()
        self.assertFalse(any(c[0] == new_customer_id for c in customers_after))

    def test_remove_customer_not_found(self):
        with self.assertRaises(CustomerNotFoundException):
            self.repo.removeCustomer(999999)  # unlikely to exist

    def test_find_customer_not_found(self):
        customer = self.repo.findCustomerById(999999)
        self.assertIsNone(customer)  # or assertRaises if you throw exception

if __name__ == "__main__":
    unittest.main()
