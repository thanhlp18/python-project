
import mysql.connector

try:
    database = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
    )
    # If connection is successful, perform operations here
    cursor = database.cursor()
    # Execute queries, fetch data, etc.
    cursor.execute("CREATE DATABASE StudentManagement")
    # Fetch results, process data, etc.
   
    # Close the connection
    database.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
