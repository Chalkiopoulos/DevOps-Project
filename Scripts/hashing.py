import hashlib
import bcrypt

def hash_password(plaintext,algorithm):
    # this function encrypts the plaintext using the specified algorithm. I encode the passwords first.
    if algorithm == "bcrypt":
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(plaintext.encode(), salt)

    elif algorithm == "sha256":
        hash = hashlib.sha256(plaintext.encode()).hexdigest()

    elif  algorithm == "md5":
        hash = hashlib.md5(plaintext.encode()).hexdigest()

    else:   
        raise ValueError("Unsupported algorithm")    

    return(hash)

def verify_password_hash(plaintext, hashed, algorithm):
    # this function verifies the password hash using the specified algorithm
    if algorithm == "bcrypt":
        password_verified = bcrypt.checkpw(plaintext.encode(), hashed)
        if password_verified:
            return True
        else:
            return False

    elif algorithm == "sha256":
        password_verified = hashlib.sha256(plaintext.encode()).hexdigest() == hashed
        if password_verified:
            return True
        else:
            return False

    elif algorithm == "md5":
        password_verified = hashlib.md5(plaintext.encode()).hexdigest() == hashed
        if password_verified:
            return True
        else:
            return False
    else:
        raise ValueError("Unsupported algorithm")