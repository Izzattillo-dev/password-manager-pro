from cryptography.fernet import Fernet
import base64
import hashlib


def generate_key(master_password: str) -> bytes:
    """
    Master password dan barqaror shifrlash kaliti yaratadi
    """
    password_bytes = master_password.encode()
    key = hashlib.sha256(password_bytes).digest()
    return base64.urlsafe_b64encode(key)


def encrypt_password(password: str, master_password: str) -> str:
    """
    Parolni shifrlaydi
    """
    key = generate_key(master_password)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted.decode()


def decrypt_password(encrypted_password: str, master_password: str) -> str:
    """
    Shifrlangan parolni ochadi
    """
    key = generate_key(master_password)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()
