from util.db_conn_util import get_connection

try:
    conn = get_connection()
    if conn.is_connected():
        print("Connected to MySQL database successfully!")
    else:
        print("Failed to connect.")
except Exception as e:
    print("Error:", e)

