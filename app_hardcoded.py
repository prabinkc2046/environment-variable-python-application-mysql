import mysql.connector

# MySQL server configuration
db_config = {
    'host': 'localhost',
    'user': 'python',
    'password': 'python',
    'database': 'database'
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
