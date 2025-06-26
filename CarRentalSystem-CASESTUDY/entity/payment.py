class Payment:
    def __init__(self, paymentID, leaseID, paymentDate, amount):
        self.paymentID = paymentID
        self.leaseID = leaseID
        self.paymentDate = paymentDate
        self.amount = amount

    def __str__(self):
        return f"Payment {self.paymentID} - ₹{self.amount} on {self.paymentDate}"
