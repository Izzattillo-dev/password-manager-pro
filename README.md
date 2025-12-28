# 🔐 Password Manager Pro

A secure, CLI-based password manager built with **Python**.  
This project demonstrates **encryption**, **secure authentication**, and **clean architecture** using real-world development practices.

---

## 🚀 Features

- 🔑 Master password authentication
- 🧂 Salted key derivation for encryption
- 🔐 Secure password encryption & decryption
- 📦 Local encrypted storage using JSON
- ➕ Add new passwords
- 🔍 Retrieve saved passwords
- ✏️ Update existing passwords
- 🗑 Delete passwords
- 🧱 Clean and modular project structure
- 💻 CLI-based interface

---

## 🧠 Tech Stack

- Python 3
- cryptography (Fernet)
- hashlib & secrets
- JSON file storage
- Git & GitHub

---

## 📁 Project Structure

```text
password-manager-pro/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # CLI entry point
│   ├── manager.py    # Password CRUD logic
│   ├── auth.py       # Master password & verification
│   └── utils.py      # Encryption / Decryption utilities
│
├── data/
│   ├── master.json    # Encrypted master password & salt
│   └── passwords.json # Encrypted stored passwords
│
├── README.md
├── requirements.txt
└── .gitignore





