# 🔐 Password Manager Pro

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%2064--bit-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)
![Build](https://img.shields.io/badge/Build-PyInstaller-success.svg)

A **secure, real-world CLI Password Manager** built with Python.
Designed with **security-first principles**, **clean architecture**, and **practical usage** in mind.

---

## ✨ Features

* 🔐 **Master password protection**
* 🧂 **Salted & hashed master password** (PBKDF2)
* 🔒 **Encrypted password storage** (Fernet / AES)
* 📦 **100% local storage** (no cloud, no tracking)
* 🧠 Clean, modular project architecture
* 🖥️ Windows standalone `.exe` (no Python required)

---

## 📸 Demo (CLI)

Password Manager running on Windows:

![Add Password](assets/screenshot-add.png)
![Get Password](assets/screenshot-get.png)

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

## 🛡️ Security Notes

* Master password is **never stored in plain text**
* Encryption key is derived using **PBKDF2 + salt**
* Passwords are encrypted using **industry‑standard cryptography**
* All data remains **fully local** on your machine

⚠️ This project is for **educational and portfolio purposes**.
It is **not recommended for production use** without a professional security audit.

---

## 🧩 Project Structure

```text
password-manager-pro/
├── app/
│   ├── auth.py        # Master password logic
│   ├── manager.py    # Password CRUD operations
│   ├── utils.py      # Encryption & helpers
│   └── main.py       # CLI entry point
├── assets/            # Screenshots & demo images
├── dist/              # Windows executable
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

## 🚀 Roadmap

* [ ] Cross‑platform support (Linux)
* [ ] Password strength meter
* [ ] Auto‑lock timeout
* [ ] Encrypted backup export

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Built with ❤️ by **Izzattillo‑dev**
Focused on real‑world Python projects, security, and clean engineering.

🔗 GitHub: [https://github.com/Izzattillo-dev](https://github.com/Izzattillo-dev)












