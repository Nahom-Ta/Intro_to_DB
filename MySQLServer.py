import mysql.connector  # Import MySQL connector

connection = None  # Initialize connection variable

try:
    # Establish connection
    connection = mysql.connector.connect(
        host='localhost',  # Change if necessary
        user='your_username',  # Replace with your MySQL username
        password='your_password'  # Replace with your MySQL password
    )
    print("Connection to MySQL server successful!")

    # Create cursor
    cursor = connection.cursor()
    
    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")  # Handle errors

finally:
    if connection and connection.is_connected():  # Check if connection is open
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        print("MySQL connection is closed.")
