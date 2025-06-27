import openpyxl
from datetime import datetime

test_results = [
    ("test_add_customer", "test_customer.py", "Add a valid customer", "Customer added", "Customer added", "Pass"),
    ("test_remove_customer_not_found", "test_customer.py", "Remove customer with invalid ID", "Raise Exception", "Exception raised", "Pass"),
    ("test_create_lease", "test_lease.py", "Create lease for valid data", "Lease created", "Lease created", "Pass"),
    ("test_record_payment", "test_payment.py", "Record lease payment", "Payment saved", "Payment saved", "Pass"),
    ("test_find_vehicle_not_found", "test_vehicle.py", "Find non-existent vehicle", "Raise Exception", "Exception raised", "Pass"),
]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Unit Test Report"

headers = ["Test Name", "Module", "Description", "Expected Outcome", "Actual Outcome", "Status"]
ws.append(headers)

for result in test_results:
    ws.append(result)

filename = f"Unit_Test_Report_{datetime.today().strftime('%Y-%m-%d')}.xlsx"
wb.save(filename)
print(f"Report saved as {filename}")
