#  File Encryption & Decryption Tool (Password-Protected)
##  Project Overview

This is a simple Python-based file encryption and decryption tool using the `cryptography` library. It allows you to:

- Generate secure encryption keys.
- encrypt sensitive files.
- Decrypt files with password authentication

---

# How It Works

1. ** Key Generation** ('generate_key.py'):
2. **File Encryption** ('file.encryptor.py'):
- Prompts for a password.
- Encrypts your chosen file using the generated key.
- Saves the encrypted output as 'yourfile.encrypted'.
3. ** File Decryption** ('decrypt_file.py'):
- Prompts for the same password.
- Uses the stored key to decrypt the file.
- Outputs the original content.

---
## Prerequisites

- Python 3.10 or above
- 'cryptography' module installed:
  '''bash
 pip install crytography

---
## How to use
1. Generate Key (python3 generate_key.py)
2. Encrypt a file ( python3 file.encryptor.py)
3. Decrypt the file ( python3 decrypt_file.py)

Enter the same password to decrypt
Files included
- generate_key.py
- file.encryptor.py
- decrypt_file.py
- key.key
- README.md

---
## Warning
- This tool is for educational purposes only.
- Do not expose your key (key.key) in public repositories
- Use strong passwords for better security

## Author
Built with love by a future CyberSecurity Analyst learning through hands-on labs. 
