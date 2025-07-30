from cryptography.fernet import Fernet
from encryption import encrypt
from encryption import decrypt
from create_key import create_key
from encryption_list import encrypt_list
from encryption_list import decrypt_list
import os
import pyfiglet


A=["123456","password","123456789","12345678","12345","qwerty","abc123","football","monkey","letmein","admin","welcome","login","princess","dragon","passw0rd","master","hello","freedom","whatever","qazwsx","trustno1","654321","123123"]

C=encrypt_list(A)

# write the encrypted passwords in a file

with open('encrypted_passwords.txt', 'w') as f:
    for cypher in C:
        cyphertext = cypher.decode()
        f.write(f"{cyphertext}\n")

# this plays with the pyfiglet lib 

ascii_banner = pyfiglet.figlet_format("CI/CD IS COOL")
print(ascii_banner)