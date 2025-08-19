import mysql.connector
from hashing import hash_password
import pyfiglet
import os
import dotenv


dotenv_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path)



db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT", "3306"))

print(f"Trying to resolve host: {db_host}:{db_port}")

# Connect to the MySQL container
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)


cursor = connection.cursor()

with open("testing_passwords.txt", "r") as f:       #reads the passwords
    passwords = [line.strip() for line in f]


for password in passwords:
    md5_hash = hash_password(password, "md5")
    sha256_hash = hash_password(password, "sha256")
    bcrypt_hash = hash_password(password, "bcrypt")

    cursor.execute(
        "INSERT INTO weak_passwords (plaintext, md5_hash, sha256_hash, bcrypt_hash) VALUES (%s, %s, %s, %s)",
        (password, md5_hash, sha256_hash, bcrypt_hash)
    )
connection.commit()

cursor.execute("SELECT * FROM weak_passwords;")
for row in cursor.fetchall():
    print(row)



# Cleanup
cursor.close()
connection.close()

ascii_banner = pyfiglet.figlet_format("DATABASES ARE COOL")
print(ascii_banner)