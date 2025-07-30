from cryptography.fernet import Fernet
from encryption import encrypt
from encryption import decrypt
from create_key import create_key
from encryption_list import encrypt_list
from encryption_list import decrypt_list
import pyfiglet
import os
# this is a mock test to check if encryption is running fine before writing to the file

A=["123456","password","123456789","12345678","12345","qwerty","abc123","football","monkey","letmein","admin","welcome","login","princess","dragon","passw0rd","master","hello","freedom","whatever","qazwsx","trustno1","654321","123123"]
C=[]
P=[]

print(A)
C=encrypt_list(A)
print(C)
#P = decrypt_list(C)
print(P)

if A!=P:
    raise Exception("Encryption went wrong")

# this plays with the pyfiglet lib 

ascii_banner = pyfiglet.figlet_format("TESTS ARE COOL")
print(ascii_banner)