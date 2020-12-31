from cryptography.fernet import Fernet

def decrypt(filename, key):
    fernClass = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    new_filename = filename.split(".")[0] + "_decrypted.txt"
    with open(new_filename, "wb") as file:
        file.write(decrypted_data)
