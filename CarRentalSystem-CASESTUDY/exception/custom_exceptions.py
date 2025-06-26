# exception/custom_exceptions.py

class CustomerNotFoundException(Exception):
    def __init__(self, customerID):
        super().__init__(f"Customer with ID {customerID} not found.")

class VehicleNotFoundException(Exception):
    def __init__(self, vehicleID):
        super().__init__(f"Vehicle with ID {vehicleID} not found.")

class LeaseNotFoundException(Exception):
    def __init__(self, leaseID):
        super().__init__(f"Lease with ID {leaseID} not found.")
