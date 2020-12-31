from cryptography.fernet import Fernet
#Fernet is a implementation of symmetric AE

def write_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()
