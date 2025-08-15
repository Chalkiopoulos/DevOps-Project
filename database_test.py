import mysql.connector

# Connect to the MySQL container
connection = mysql.connector.connect(
    host="localhost",      
    port=3306,
    user="root",
    password="my-secret-pw",
    database="mysql"        
)

cursor = connection.cursor()

cursor.execute("SELECT VERSION();")

# Fetch and print result
version = cursor.fetchone()
print("MySQL version:", version[0])

# Cleanup
cursor.close()
connection.close()