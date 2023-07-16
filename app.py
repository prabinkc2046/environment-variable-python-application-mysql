import mysql.connector
import os

# MySQL server configuration
db_config = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME')
}

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Connected to MySQL server")
        # Perform database operations...
        connection.close()
        print("MySQL connection closed")
    else:
        print("Failed to connect to MySQL server")
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL server: {err}")
