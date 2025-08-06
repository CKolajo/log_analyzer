from cryptography.fernet import Fernet
from getpass import getpass

# Load the key from file
with open("key.key", "rb") as key_file:
  key = key_file.read()

fernet = Fernet(key)

# Ask for a password (same one used for encryption)
user_password = getpass("Enter decryption password:")

# Read the encrypted file
with open("secret.txt.encrypted", "rb") as encrypted_file:
  encrypted_data = encrypted_file.read()

decrypted = fernet.decrypt(encrypted_data)

# Save the decrypted content
with open("secret_decrypted.txt", "wb") as decrypted_file:
  decrypted_file.write(decrypted)

print("Decryption successful.")
