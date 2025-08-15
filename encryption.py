from cryptography.fernet import Fernet
from create_key import create_key
import os

def encrypt(plaintext):
    #generate the encryption key if it doesnt exist, this checks if it already exists
    if not os.path.exists("filekey.key"):
        raise FileNotFoundError("Key file does not exist, cannot encrypt")

    #load the key
    with open("filekey.key", "rb") as key_file:
        key = key_file.read()
    f=Fernet(key)

    #encrypt the plaintext
    byte_plaintext = plaintext.encode()
    cyphertext = f.encrypt(byte_plaintext)

    return(cyphertext)

def decrypt(cyphertext):
#this checks if the key exists
    if not os.path.exists("filekey.key"):
        print("Key file does not exist, cannot decrypt")
        return
    
    with open("filekey.key", "rb") as key_file:
        key = key_file.read()
    f=Fernet(key)

    decrypted = f.decrypt(cyphertext)
    return(decrypted.decode())