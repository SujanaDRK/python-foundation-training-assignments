# tests/test_vehicle.py

import unittest
from entity.vehicle import Vehicle
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl

class TestVehicleOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepositoryImpl()
        cls.test_vehicle = Vehicle(0, "TestBrand", "TestModel", 2024, 1500.0, "available", 5, 2.0)

    def test_add_vehicle(self):
        self.repo.addCar(self.test_vehicle)
        available = self.repo.listAvailableCars()
        self.assertTrue(any(v[1] == "TestBrand" for v in available))

    def test_list_available_vehicles(self):
        result = self.repo.listAvailableCars()
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
