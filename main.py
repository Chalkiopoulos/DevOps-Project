from cryptography.fernet import Fernet
from encryption import encrypt
from encryption import decrypt
from create_key import create_key

#an array of common and weak passwords

A=["123456","password","123456789","12345678","12345","qwerty","abc123","football","monkey","letmein","admin","welcome","login","princess","dragon","passw0rd","master","hello","freedom","whatever","qazwsx","trustno1","654321","123123"]

plaintext= input("Type the phrase you want to encrypt: ")
print("You typed", plaintext)

c=encrypt(plaintext)
print("Your encrypted message is: ", c)

p=decrypt(c)

print("Your decrypted message is: ", p)

