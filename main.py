from cryptography.fernet import Fernet
from encryption import encrypt
from encryption import decrypt
from create_key import create_key
from encryption_list import encrypt_list
from encryption_list import decrypt_list
import os
import pyfiglet

with open("passwords.txt", "r") as f:       #reads the passwords
    passwords = [line.strip() for line in f]

C=encrypt_list(passwords)
# write the encrypted passwords in a file

with open('encrypted_passwords.txt', 'w') as f:
    for cypher in C:
        cyphertext = cypher.decode()
        f.write(f"{cyphertext}\n")

# this plays with the pyfiglet lib 

ascii_banner = pyfiglet.figlet_format("CI/CD IS COOL")
print(ascii_banner)
