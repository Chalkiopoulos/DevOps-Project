from cryptography.fernet import Fernet
import os

plaintext_names = ["nick", "alex", "thanos", "makis"]
encrypted_names = []

#sort the names
list.sort(plaintext_names)

#print the plaintext names
print("the plaintext names are: ")
for name in plaintext_names:
    print(name)

#generate the encryption key if it doesnt exist
if not os.path.exists("filekey.key"):
    create_key()


#load the key
with open("filekey.key", "rb") as key_file:
    key = key_file.read()
f=Fernet(key)

#encrypt the names

for name in plaintext_names:
    b_name= name.encode()
    k=f.encrypt(b_name)
    encrypted_names.append(k)

#print encrypted names
print("the encrypted names are: ") 
for name in encrypted_names:
    print(name)