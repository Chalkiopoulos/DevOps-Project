from cryptography.fernet import Fernet
from encryption import encrypt
from encryption import decrypt
from create_key import create_key
from encryption_list import encrypt_list
from encryption_list import decrypt_list
import pyfiglet
import os
# this is a mock test to check if encryption is running fine before writing to the file

create_key()
with open("passwords.txt", "r") as f:       #reads the passwords
    passwords = [line.strip() for line in f]

C=[]
P=[]

print(passwords)
C=encrypt_list(passwords)
print(C)
P = decrypt_list(C)
print(P)

if passwords!=P:
    raise Exception("Encryption went wrong")

print("Encryption worked")

# this plays with the pyfiglet lib 

ascii_banner = pyfiglet.figlet_format("TESTS ARE COOL")
print(ascii_banner)