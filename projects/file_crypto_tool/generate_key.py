from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os
from getpass import getpass

# Prompt for password
password = getpass("Enter a password to generate encryption key:").encode()

# Generate a random salt
salt = os.urandom(16)

# Use PBKDF2HMAC  to derive a secure key from the password
kdf = PBKDF2HMAC(
  algorithm = 'SHA256',
  length = 32,
  salt = salt,
  iterations = 100000,
  backend = default_backend()
)

key =base64.urlsafe_b64encode(kdf.derive(password))

# Save the salt and key to a file
with open("key.key", "wb") as key_file:
   key_file.write(salt + b":"+ key)

print("Key generated and saved to 'key.key'")
