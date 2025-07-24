from cryptography.fernet import Fernet
from encryption import encrypt
from create_key import create_key


plaintext= input("Type the phrase you want to encrypt: ")
print("You typed", plaintext)

encrypt(plaintext)


