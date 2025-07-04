import mysql.connector
from util.db_property_util import get_property_string

def get_connection():
    props = get_property_string(
        r"C:\Users\sujan\Downloads\python-foundation-training-assignments\CarRentalSystem-CASESTUDY\db.properties")

    conn = mysql.connector.connect(
        host=props['host'],
        port=int(props['port']),
        user=props['username'],
        password=props['password'],
        database=props['dbname']
    )

    return conn
