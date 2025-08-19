
import pyfiglet
import os
from hashing import hash_password, verify_password_hash
import dotenv

#THE MAIN FUNCTION IN INCOMPLETE NOW JUST MAKES A FILE OF THE HASHES


with open("testing_passwords.txt", "r") as f:       #reads the passwords
    passwords = [line.strip() for line in f]


for password in passwords:
    md5_hash = hash_password(password, "md5")
    sha256_hash = hash_password(password, "sha256")
    bcrypt_hash = hash_password(password, "bcrypt")
    with open("hashed_passwords.txt", "a") as f:  #appends the hashes to a file
        f.write(f"Password: {password}\n")
        f.write(f"MD5: {md5_hash}\n")
        f.write(f"SHA256: {sha256_hash}\n")
        f.write(f"Bcrypt: {bcrypt_hash}\n\n")
        
# this plays with the pyfiglet lib
ascii_banner = pyfiglet.figlet_format("GitHub actions are COOL")
print(ascii_banner)
