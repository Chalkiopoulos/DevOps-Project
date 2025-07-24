from cryptography.fernet import Fernet


# Step 1: Generate the key
key = Fernet.generate_key()

# Step 2: Save the key to a file
with open("filekey.key", "wb") as key_file:
    key_file.write(key)

print("Key generated and saved to 'filekey.key'")
