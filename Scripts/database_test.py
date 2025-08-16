import mysql.connector
from encryption import encrypt
import pyfiglet
import os
import dotenv


dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)

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

    

# Cleanup
cursor.close()
connection.close()

ascii_banner = pyfiglet.figlet_format("DATABASES ARE COOL")
print(ascii_banner)