class Customer:
    def __init__(self, customerID, firstName, lastName, email, phoneNumber):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"{self.customerID}: {self.firstName} {self.lastName} - {self.email} ({self.phoneNumber})"
