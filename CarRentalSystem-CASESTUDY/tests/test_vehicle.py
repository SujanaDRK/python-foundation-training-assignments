# tests/test_vehicle.py
import unittest
from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl
from exception.custom_exceptions import VehicleNotFoundException

class TestVehicleOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepositoryImpl()

    def test_remove_vehicle_not_found(self):
        with self.assertRaises(VehicleNotFoundException):
            self.repo.removeCar(999999)

    def test_find_vehicle_not_found(self):
        with self.assertRaises(VehicleNotFoundException):
            self.repo.findCarById(999999)
 

if __name__ == "__main__":
    unittest.main()
