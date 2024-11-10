#To make Database credentials to safer be used a encryption file..
from cryptography.fernet import Fernet
# Generate a key 
key = Fernet.generate_key()
cipher = Fernet(key)

# Database credentials
db_credentials = {
    'USER': 'root',
    'PASSWORD': 'm@ssMohan09',
    'HOST': 'localhost',
    'PORT': '3306',
    'NAME': 'resume_form_db'
}

# Encrypting each value
encrypted_credentials = {key: cipher.encrypt(value.encode()).decode() for key, value in db_credentials.items()}
# Store the encrypted credentials
with open('encrypted_db_credentials.txt', 'w') as f:
    f.write(f"{key.decode()}\n")
    for key, encrypted_value in encrypted_credentials.items():
        f.write(f"{key}: {encrypted_value}\n")
print("Credentials encrypted and saved.")
