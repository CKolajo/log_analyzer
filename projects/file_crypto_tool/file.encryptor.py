from cryptography.fernet import Fernet
from getpass import getpass

# Load the key from file
with open("key.key", "rb") as key_file:
  key = key_file.read()

# Ask for a password
user_password = getpass("Enter encryption password:")

# Encrypt the contents of a file
fernet = Fernet(key)

with open("secret.txt", "rb") as file:
  original = file.read()

# Encrypt the contents
encrypted = fernet.encrypt(original)

with open("secret.txt.encrypted", "wb") as encrypted_file:
  encrypted_file.write(encrypted)

print("File encrypted successfully.")
