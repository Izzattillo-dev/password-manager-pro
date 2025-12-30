## 👋 Hi, I'm Izzattillo

🚀 Junior Python Developer | Security-focused learner

I’m learning Python by building real-world projects with a strong focus on:
- clean architecture
- security best practices
- practical CLI tools

---

### 🔐 Featured Project

**Password Manager Pro**  
A secure CLI-based password manager built with Python.

🔹 Master password authentication  
🔹 PBKDF2 + salt-based encryption  
🔹 Secure local storage  
🔹 CRUD operations (Add / Get / Update / Delete)  

👉 [View Project Repository](https://github.com/Izzattillo-dev/password-manager-pro)

---

### 🧠 Tech Stack

- Python
- cryptography (Fernet)
- hashlib / PBKDF2
- JSON
- Git & GitHub

---

### 📌 Currently Learning

- Secure application design
- Encryption & key derivation
- Python project structuring
- Git best practices

---

### 📫 Contact

- GitHub: https://github.com/Izzattillo-dev

---

⭐ Always improving. Always building.

# 🔐 Password Manager Pro

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%2064--bit-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)
![Build](https://img.shields.io/badge/Build-PyInstaller-success.svg)

A **secure, real-world CLI Password Manager** built with Python.
Designed with security-first principles, clean architecture, and real usage in mind.

---

## ✨ Features

* 🔐 **Master Password Protection**
* 🧂 **Salted & hashed master password**
* 🔒 **Encrypted password storage** (AES via `cryptography`)
* 📦 Local secure storage (no cloud, no tracking)
* 🧠 Clean modular architecture
* 🖥️ Windows standalone `.exe` (no Python required)

---

## 🖥️ Platform

* **OS:** Windows (64-bit)
* **Python:** 3.11+
* **Build Tool:** PyInstaller

---

## 🚀 How to Use (Windows)

1. Download `PasswordManagerPro_v1.0_windows.zip`
2. Extract the archive
3. Run `main.exe`
4. Create your master password
5. Start managing your passwords securely

---

## 📸 Demo (CLI Preview)

```text
🔑 Welcome to Password Manager
Enter master password:

1. Add new password
2. Get password
3. Update password
4. Delete password
5. Generate strong password
6. Exit
```

---

## 🛡️ Security Notes

* Master password is **never stored in plain text**
* Passwords are encrypted using **industry-standard cryptography**
* Encryption key is derived securely from the master password
* All data remains **100% local** on your machine

⚠️ This project is for **educational and portfolio purposes**.
Not recommended for production use without security audit.

---

## 🧩 Project Structure

```text
password-manager-pro/
├── app/
│   ├── auth.py
│   ├── manager.py
│   ├── utils.py
│   └── main.py
├── dist/
│   └── main.exe
├── README.md
└── requirements.txt
```

---

## 📦 Build From Source

```bash
pip install -r requirements.txt
python -m PyInstaller --onefile app/main.py
```

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Built with ❤️ by **Izzattillo-dev**
Focused on real-world Python projects & clean engineering.

🔗 GitHub: [https://github.com/Izzattillo-dev](https://github.com/Izzattillo-dev)

## 📸 Demo

![Start](assets/screenshot-1.png)
![Menu](assets/screenshot-2.png)

## 📸 Demo

![Password Manager CLI](assets/screenshot-1.png)


