import mysql.connector  # Import MySQL connector

# Initialize connection variable
connection = None  

try:
    # Establish connection to the MySQL server
    connection = mysql.connector.connect(
        host='localhost',  # Change if necessary
        user='your_actual_username',  # Replace with your MySQL username (e.g., 'root')
        password='your_actual_password'  # Replace with your MySQL password
    )
    print("Connection to MySQL server successful!")

    # Create cursor
    cursor = connection.cursor()
    
    # Create database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")  # Handle errors

finally:
    if connection and connection.is_connected():  # Check if connection is open
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        print("MySQL connection is closed.")
