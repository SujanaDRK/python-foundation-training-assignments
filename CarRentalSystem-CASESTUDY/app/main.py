import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.icar_lease_repository_impl import ICarLeaseRepositoryImpl
from entity.customer import Customer
from entity.vehicle import Vehicle
from exception.custom_exceptions import CustomerNotFoundException, VehicleNotFoundException, LeaseNotFoundException

def main():
    repo = ICarLeaseRepositoryImpl()

    while True:
        print("\n====== CAR RENTAL SYSTEM MENU ======")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. Add Vehicle")
        print("4. View Available Vehicles")
        print("5. Create Lease")
        print("6. Return Car")
        print("7. Record Payment")
        print("8. View Active Leases")
        print("9. View Lease History")
        print("10. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                first = input("First name: ")
                last = input("Last name: ")
                email = input("Email: ")
                phone = input("Phone number: ")
                customer = Customer(0, first, last, email, phone)
                repo.addCustomer(customer)

            elif choice == "2":
                cid = int(input("Customer ID to remove: "))
                repo.removeCustomer(cid)

            elif choice == "3":
                make = input("Make: ")
                model = input("Model: ")
                year = int(input("Year: "))
                rate = float(input("Daily Rate: "))
                status = "available"
                capacity = int(input("Passenger Capacity: "))
                engine = float(input("Engine Capacity: "))
                vehicle = Vehicle(0, make, model, year, rate, status, capacity, engine)
                repo.addCar(vehicle)

            elif choice == "4":
                available = repo.listAvailableCars()
                print("\nAvailable Cars:")
                for v in available:
                    print(v)

            elif choice == "5":
                cid = int(input("Customer ID: "))
                vid = int(input("Vehicle ID: "))
                start = input("Start date (YYYY-MM-DD): ")
                end = input("End date (YYYY-MM-DD): ")
                repo.createLease(cid, vid, start, end)

            elif choice == "6":
                lease_id = int(input("Lease ID to return: "))
                repo.returnCar(lease_id)

            elif choice == "7":
                lease_id = int(input("Lease ID: "))
                amount = float(input("Payment Amount: "))
                repo.recordPayment(lease_id, amount)

            elif choice == "8":
                leases = repo.listActiveLeases()
                print("\nActive Leases:")
                for lease in leases:
                    print(lease)

            elif choice == "9":
                history = repo.listLeaseHistory()
                print("\nLease History:")
                for lease in history:
                    print(lease)

            elif choice == "10":
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid option. Try again.")

        except CustomerNotFoundException as e:
            print(f"Error: {e}")
        except VehicleNotFoundException as e:
            print(f"Error: {e}")
        except LeaseNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
