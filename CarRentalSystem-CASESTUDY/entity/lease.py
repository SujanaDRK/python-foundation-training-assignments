class Lease:
    def __init__(self, leaseID, vehicleID, customerID, startDate, endDate, leaseType):
        self.leaseID = leaseID
        self.vehicleID = vehicleID
        self.customerID = customerID
        self.startDate = startDate
        self.endDate = endDate
        self.leaseType = leaseType

    def __str__(self):
        return f"Lease {self.leaseID} (Customer {self.customerID} - Vehicle {self.vehicleID})"
