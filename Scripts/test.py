import hashlib
from hashing import hash_password, verify_password_hash
import pyfiglet
import os
# this is a mock test to check if hashing algorithms run fine

with open("testing_passwords.txt", "r") as f:       #reads the passwords
    passwords = [line.strip() for line in f]


test_password = "123456"

bcrypt_hash = (hash_password(test_password, "bcrypt"))
sha256_hash = (hash_password(test_password, "sha256"))
md5_hash = (hash_password(test_password, "md5"))

bcrypt_verify = verify_password_hash(test_password, bcrypt_hash, "bcrypt")
sha256_verify = verify_password_hash(test_password, sha256_hash, "sha256")
md5_verify = verify_password_hash(test_password, md5_hash, "md5")


assert bcrypt_verify and sha256_verify and md5_verify
        
for password in passwords:
    print(f"Testing password: {password}")
    bcrypt_hash = hash_password(password, "bcrypt")
    sha256_hash = hash_password(password, "sha256")
    md5_hash = hash_password(password, "md5")

    assert verify_password_hash(password, bcrypt_hash, "bcrypt"), f"Bcrypt verification failed for {password}"
    assert verify_password_hash(password, sha256_hash, "sha256"), f"SHA256 verification failed for {password}"
    assert verify_password_hash(password, md5_hash, "md5"), f"MD5 verification failed for {password}"

# this plays with the pyfiglet lib 

ascii_banner = pyfiglet.figlet_format("TESTS ARE COOL")
print(ascii_banner)