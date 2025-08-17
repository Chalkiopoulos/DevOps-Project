import mysql.connector
from encryption import encrypt
import pyfiglet
import os
import socket
import dotenv


dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)



db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT", "3306"))

print(f"Trying to resolve host: {db_host}:{db_port}")

try:
    ip = socket.gethostbyname(db_host)
    print(f" Host '{db_host}' resolves to {ip}")

    # Test TCP connection
    with socket.create_connection((db_host, db_port), timeout=5):
        print(f" Successfully connected to {db_host}:{db_port} at TCP level")

except socket.gaierror as e:
    print(f" Hostname resolution failed for {db_host}: {e}")
except socket.error as e:
    print(f" TCP connection to {db_host}:{db_port} failed: {e}")

# Connect to the MySQL container
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)


    #load the key
with open("filekey.key", "rb") as key_file:
    enc_key = key_file.read()

cursor = connection.cursor()

cursor.execute("SELECT * FROM plaintexts;")



# Fetch and print result
for row in cursor.fetchall():
    print(row[1]) # only want the the second element of the tuple that fetchall() returns
    cyphertext=encrypt(row[1])  # Encrypt the plaintext value

    print(cyphertext)
    cursor.execute(
        "INSERT INTO encryptions (plaintext_id, key_value, encryption_value) VALUES (%s, %s, %s)",
        (row[0], enc_key, cyphertext)
    )
connection.commit()

cursor.execute("SELECT * FROM encryptions;")
for row in cursor.fetchall():
    print(row)

# Cleanup
cursor.close()
connection.close()

ascii_banner = pyfiglet.figlet_format("DATABASES ARE COOL")
print(ascii_banner)