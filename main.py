from cryptography.fernet import Fernet
from encryption import encrypt
from encryption import decrypt
from create_key import create_key
from encryption_list import encrypt_list
from encryption_list import decrypt_list

A = ["nick","makis","takis","pakis"]

print(A)
C=encrypt_list(A)
print(C)
P=decrypt_list(C)
print(P)