import keyGen
import sys
from cryptography.fernet import Fernet

def encrypt(filename, key):
    fernClass = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = fernClass.encrypt(file_data)
    new_filename = filename.split(".")[0] + "_encrypted.txt"

    with open(new_filename, "wb") as file:
        file.write(encrypted_data)

keyGen.write_key() # calling this generates a new key using Fernet
            # and saves this generated key to file

key = keyGen.load_key() # now load this key from where we just saved it to

filename = sys.argv[1] # retrieve filename from command line arg

encrypt(filename, key)
