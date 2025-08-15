from cryptography.fernet import Fernet
from create_key import create_key
import os

def encrypt_list(list):
    cyphertext_list=[]
    #generate the encryption key if it doesnt exist, this checks if it already exists
    

    if not os.path.exists("filekey.key"):
        raise FileNotFoundError("Key file does not exist, cannot encrypt")

    #load the key
    with open("filekey.key", "rb") as key_file:
        key = key_file.read()
    f=Fernet(key)

    #encrypt the plaintext
    for plaintext in list:
        byte_plaintext = plaintext.encode()
        cyphertext = f.encrypt(byte_plaintext)
        cyphertext_list.append(cyphertext)
    return(cyphertext_list)




def decrypt_list(list):
    plaintext_list=[]

    #this checks if the key exists
    if not os.path.exists("filekey.key"):
        print("Key file does not exist, cannot decrypt")
        return
    
    with open("filekey.key", "rb") as key_file:
        key = key_file.read()
    f=Fernet(key)

    for cyphertext in list:
        byte_text=f.decrypt(cyphertext)
        plaintext=byte_text.decode()
        plaintext_list.append(plaintext)

    return(plaintext_list)