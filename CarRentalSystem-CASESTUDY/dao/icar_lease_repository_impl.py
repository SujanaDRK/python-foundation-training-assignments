from dao.icar_lease_repository import ICarLeaseRepository
from util.db_conn_util import get_connection
from entity.customer import Customer
from entity.vehicle import Vehicle
from entity.lease import Lease
from entity.payment import Payment
from exception.custom_exceptions import CustomerNotFoundException


class ICarLeaseRepositoryImpl(ICarLeaseRepository):

    # -------------------------------
    # CUSTOMER OPERATIONS
    # -------------------------------

    def addCustomer(self, customer):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO Customer (firstName, lastName, email, phoneNumber)
            VALUES (%s, %s, %s, %s)
            """
            data = (customer.firstName, customer.lastName, customer.email, customer.phoneNumber)
            cursor.execute(query, data)
            conn.commit()
            print("Customer added successfully!")

        except Exception as e:
            print("Error adding customer:", e)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def removeCustomer(self, customerID):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM Lease WHERE customerID = %s", (customerID,))
            lease_count = cursor.fetchone()[0]

            if lease_count > 0:
                print(f"Cannot delete: Customer ID {customerID} has active or historical leases.")
                return

            cursor.execute("DELETE FROM Customer WHERE customerID = %s", (customerID,))
            conn.commit()

            if cursor.rowcount == 0:
               raise CustomerNotFoundException(customerID)

            else:
                print(f"Customer ID {customerID} removed successfully.")

        except Exception as e:
            print("Error removing customer:", e)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listCustomers(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer")
            customers = cursor.fetchall()
            return customers
        except Exception as e:
            print("Error listing customers:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def findCustomerById(self, customerID):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE customerID = %s", (customerID,))
            customer = cursor.fetchone()
            return customer
        except Exception as e:
            print("Error finding customer:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # -------------------------------
    # VEHICLE OPERATIONS
    # -------------------------------

    def addCar(self, car):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            data = (car.make, car.model, car.year, car.dailyRate, car.status, car.passengerCapacity, car.engineCapacity)
            cursor.execute(query, data)
            conn.commit()
            print("Vehicle added successfully!")
        except Exception as e:
            print("Error adding vehicle:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def removeCar(self, carID):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Vehicle WHERE vehicleID = %s", (carID,))
            conn.commit()
            if cursor.rowcount == 0:
                print(f"Car ID {carID} not found.")
            else:
                print(f"Car ID {carID} removed successfully.")
        except Exception as e:
            print("Error removing vehicle:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listAvailableCars(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE status = 'available'")
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error fetching available vehicles:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listRentedCars(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT V.* FROM Vehicle V
                JOIN Lease L ON V.vehicleID = L.vehicleID
                WHERE CURDATE() BETWEEN L.startDate AND L.endDate
            """)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error fetching rented vehicles:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def findCarById(self, carID):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE vehicleID = %s", (carID,))
            car = cursor.fetchone()
            return car
        except Exception as e:
            print("Error finding vehicle:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # -------------------------------
    # LEASE OPERATIONS
    # -------------------------------

    def createLease(self, customerID, carID, startDate, endDate):
        try:
            conn = get_connection()
            cursor = conn.cursor()

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

        except Exception as e:
            print("Error creating lease:", e)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def returnCar(self, leaseID):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT vehicleID FROM Lease WHERE leaseID = %s", (leaseID,))
            result = cursor.fetchone()
            if result is None:
                print(f"No lease found with ID {leaseID}")
                return
            vehicleID = result[0]

            cursor.execute("UPDATE Lease SET endDate = CURDATE() WHERE leaseID = %s", (leaseID,))
            cursor.execute("UPDATE Vehicle SET status = 'available' WHERE vehicleID = %s", (vehicleID,))
            conn.commit()

            print("Car returned successfully.")

        except Exception as e:
            print("Error returning car:", e)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listActiveLeases(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Lease WHERE CURDATE() BETWEEN startDate AND endDate"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error fetching active leases:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def listLeaseHistory(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Lease WHERE endDate < CURDATE()"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("Error fetching lease history:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    # -------------------------------
    # PAYMENT OPERATIONS
    # -------------------------------

    def recordPayment(self, lease, amount):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO Payment (leaseID, paymentDate, amount)
                VALUES (%s, CURDATE(), %s)
            """
            cursor.execute(query, (lease, amount))
            conn.commit()
            print("Payment recorded successfully.")
        except Exception as e:
            print("Error recording payment:", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
