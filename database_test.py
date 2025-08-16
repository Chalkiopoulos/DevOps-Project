import mysql.connector
from encryption import encrypt

# Connect to the MySQL container
connection = mysql.connector.connect(
    host="localhost",      
    port=3306,
    user="root",
    password="my_secret_pw",
    database="devopsdb"
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