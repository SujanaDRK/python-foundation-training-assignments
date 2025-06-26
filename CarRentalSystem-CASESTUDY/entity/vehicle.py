class Vehicle:
    def __init__(self, vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity):
        self.vehicleID = vehicleID
        self.make = make
        self.model = model
        self.year = year
        self.dailyRate = dailyRate
        self.status = status
        self.passengerCapacity = passengerCapacity
        self.engineCapacity = engineCapacity

    def __str__(self):
        return f"{self.vehicleID}: {self.make} {self.model} - ₹{self.dailyRate}/day - {self.status}"
