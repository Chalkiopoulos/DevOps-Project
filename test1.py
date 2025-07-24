from cryptography.fernet import Fernet

plaintext_names = ["nick", "alex", "thanos", "makis"]
encrypted_names = []

list.sort(plaintext_names) # sort the names

#generate the encryption key

key = Fernet.generate_key()
f=Fernet(key)
print("the key in use is ", key)

#print the plaintext names
print("the plaintext names are: ")
for name in plaintext_names:
    print(name)

#encrypt the names

for name in plaintext_names:
    b_name= name.encode()
    k=f.encrypt(b_name)
    encrypted_names.append(k)

#print encrypted names
print("the encrypted names are: ") 
for name in encrypted_names:
    print(name)
