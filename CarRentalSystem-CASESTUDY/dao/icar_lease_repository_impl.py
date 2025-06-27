from dao.icar_lease_repository import ICarLeaseRepository
from util.db_conn_util import get_connection
from entity.customer import Customer
from entity.vehicle import Vehicle
from entity.lease import Lease
from entity.payment import Payment
from exception.custom_exceptions import CustomerNotFoundException, VehicleNotFoundException, LeaseNotFoundException

class ICarLeaseRepositoryImpl(ICarLeaseRepository):

    # -------------------------------
    # CUSTOMER OPERATIONS
    # -------------------------------

    def addCustomer(self, customer):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
            INSERT INTO Customer (firstName, lastName, email, phoneNumber)
            VALUES (%s, %s, %s, %s)
            """
            data = (customer.firstName, customer.lastName, customer.email, customer.phoneNumber)
            cursor.execute(query, data)
            conn.commit()
            print("Customer added successfully!")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def removeCustomer(self, customerID):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM Lease WHERE customerID = %s", (customerID,))
            lease_count = cursor.fetchone()[0]
            if lease_count > 0:
                print(f"Cannot delete: Customer ID {customerID} has active or historical leases.")
                return
            cursor.execute("DELETE FROM Customer WHERE customerID = %s", (customerID,))
            conn.commit()
            if cursor.rowcount == 0:
                raise CustomerNotFoundException(customerID)  # <-- Let this propagate!
            else:
                print(f"Customer ID {customerID} removed successfully.")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listCustomers(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Customer")
            customers = cursor.fetchall()
            return customers
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def findCustomerById(self, customerID):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Customer WHERE customerID = %s", (customerID,))
            customer = cursor.fetchone()
            return customer
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # -------------------------------
    # VEHICLE OPERATIONS
    # -------------------------------

    def addCar(self, car):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            data = (car.make, car.model, car.year, car.dailyRate, car.status, car.passengerCapacity, car.engineCapacity)
            cursor.execute(query, data)
            conn.commit()
            print("Vehicle added successfully!")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def removeCar(self, carID):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Vehicle WHERE vehicleID = %s", (carID,))
            conn.commit()
            if cursor.rowcount == 0:
                raise VehicleNotFoundException(carID)  # Also propagate exception for vehicles!
            else:
                print(f"Car ID {carID} removed successfully.")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listAvailableCars(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Vehicle WHERE status = 'available'")
            result = cursor.fetchall()
            return result
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listRentedCars(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT V.* FROM Vehicle V
                JOIN Lease L ON V.vehicleID = L.vehicleID
                WHERE CURDATE() BETWEEN L.startDate AND L.endDate
            """)
            result = cursor.fetchall()
            return result
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def findCarById(self, carID):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Vehicle WHERE vehicleID = %s", (carID,))
            car = cursor.fetchone()
            if not car:
                raise VehicleNotFoundException(carID)
            return car
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # -------------------------------
    # LEASE OPERATIONS
    # -------------------------------

    def createLease(self, customerID, carID, startDate, endDate):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO Lease (vehicleID, customerID, startDate, endDate, type)
                VALUES (%s, %s, %s, %s, %s)
            """
            lease_type = 'Daily'
            data = (carID, customerID, startDate, endDate, lease_type)
            cursor.execute(query, data)
            conn.commit()
            cursor.execute("UPDATE Vehicle SET status = 'notAvailable' WHERE vehicleID = %s", (carID,))
            conn.commit()
            print("Lease created successfully.")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def returnCar(self, leaseID):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT vehicleID FROM Lease WHERE leaseID = %s", (leaseID,))
            result = cursor.fetchone()
            if result is None:
                raise LeaseNotFoundException(leaseID)
            vehicleID = result[0]
            cursor.execute("UPDATE Lease SET endDate = CURDATE() WHERE leaseID = %s", (leaseID,))
            cursor.execute("UPDATE Vehicle SET status = 'available' WHERE vehicleID = %s", (vehicleID,))
            conn.commit()
            print("Car returned successfully.")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listActiveLeases(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM Lease WHERE CURDATE() BETWEEN startDate AND endDate"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listLeaseHistory(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM Lease WHERE endDate < CURDATE()"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # -------------------------------
    # PAYMENT OPERATIONS
    # -------------------------------

    def recordPayment(self, lease, amount):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO Payment (leaseID, paymentDate, amount)
                VALUES (%s, CURDATE(), %s)
            """
            cursor.execute(query, (lease, amount))
            conn.commit()
            print("Payment recorded successfully.")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
