from cryptography.fernet import Fernet
from encryption import encrypt
from encryption import decrypt
from create_key import create_key


plaintext= input("Type the phrase you want to encrypt: ")
print("You typed", plaintext)

c=encrypt(plaintext)
print("Your encrypted message is: ", c)

p=decrypt(c)

print("Your decrypted message is: ", p)

