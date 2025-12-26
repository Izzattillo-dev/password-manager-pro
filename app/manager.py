import json
import os
from app.utils import encrypt_password, decrypt_password


DATA_FILE = "data/passwords.json"


def load_passwords() -> dict:
    """
    Saqlangan parollarni fayldan o‘qiydi
    """
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_passwords(data: dict) -> None:
    """
    Parollarni faylga yozadi
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def add_password(service: str, username: str, password: str, master_password: str) -> None:
    """
    Yangi parol qo‘shadi
    """
    data = load_passwords()
    encrypted = encrypt_password(password, master_password)

    data[service] = {
        "username": username,
        "password": encrypted
    }

    save_passwords(data)


def get_password(service: str, master_password: str) -> tuple[str, str]:
    """
    Parolni ochib beradi
    """
    data = load_passwords()

    if service not in data:
        raise ValueError("Service topilmadi")

    encrypted = data[service]["password"]
    username = data[service]["username"]
    password = decrypt_password(encrypted, master_password)

    return username, password
