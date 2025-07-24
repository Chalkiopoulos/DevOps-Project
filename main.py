from cryptography.fernet import Fernet

from create_key import create_key


plaintext= input("Type the phrase you want to encrypt: ")
print("You typed", plaintext)

#generate the encryption key if it doesnt exist, this checks if it already exists

create_key()

#load the key
with open("filekey.key", "rb") as key_file:
    key = key_file.read()
f=Fernet(key)

#encrypt the plaintext
byte_plaintext = plaintext.encode()
cyphertext = f.encrypt(byte_plaintext)

print("the encrypted phrase is: ", cyphertext) 
