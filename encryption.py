from cryptography.fernet import Fernet

# Replace 'API' with encryption
encryption_key = b'z1DHJwKEsKq4PK7vNE/9RgGYiDK189yIR7xH3Ad0NpPRQmaAm2k0EZ7Hp8oDBgPppgkgke5KJQ0YFNppe+m7sA=='

def encrypt(api_key):
    cipher_suite = Fernet(encryption_key)
    encrypted_text = cipher_suite.encrypt(api_key.encode())
    return encrypted_text

def decrypt(encrypted_text):
    cipher_suite = Fernet(encryption_key)
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    return decrypted_text

