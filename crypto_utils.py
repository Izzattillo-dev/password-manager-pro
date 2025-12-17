import json
import os
import hashlib

FILE_NAME = "passwords.json"
HISTORY_FILE = "history.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_history(entry):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []
    history.append(entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)
