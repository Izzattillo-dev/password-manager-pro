from utils import load_data, save_data, hash_password, save_history, HISTORY_FILE
import os
import json

def add_password():
    account = input("Hisob nomi (Account): ")
    password = input("Parol (Password): ")
    hashed = hash_password(password)
    data = load_data()
    data.append({"account": account, "password": hashed})
    save_data(data)
    print(f"{account} uchun parol qo'shildi!")

def view_passwords():
    data = load_data()
    if not data:
        print("Hali hech qanday parol qo'shilmagan.")
        return
    for entry in data:
        print(f"Account: {entry['account']}, Hashed Password: {entry['password']}")

def delete_password():
    account = input("O'chirish uchun hisob nomini kiriting: ")
    data = load_data()
    for entry in data:
        if entry['account'] == account:
            save_history(entry)
    new_data = [entry for entry in data if entry['account'] != account]
    if len(data) == len(new_data):
        print("Bunday hisob topilmadi.")
    else:
        save_data(new_data)
        print(f"{account} o'chirildi.")

def search_password():
    query = input("Qidirish uchun hisob nomini kiriting: ")
    data = load_data()
    found = False
    for entry in data:
        if query.lower() in entry['account'].lower():
            print(f"Account: {entry['account']}, Hashed Password: {entry['password']}")
            found = True
    if not found:
        print("Bunday hisob topilmadi.")

def undo_delete():
    if not os.path.exists(HISTORY_FILE):
        print("Undo qilinadigan amal yo‘q.")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        try:
            history = json.load(file)
        except json.JSONDecodeError:
            print("Undo uchun ma'lumot yo‘q.")
            return
    if not history:
        print("Undo qilinadigan amal yo‘q.")
        return
    last_entry = history.pop()
    data = load_data()
    data.append(last_entry)
    save_data(data)
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)
    print(f"{last_entry['account']} qaytarildi!")

def menu():
    while True:
        print("\n=== Password Manager PRO ===")
        print("1. Parol qo'shish")
        print("2. Parol ko'rish")
        print("3. Parol o'chirish")
        print("4. Qidiruv")
        print("5. Undo (oxirgi o‘chirgan parolni qaytarish)")
        print("6. Chiqish")

        choice = input("Tanlovingiz: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            search_password()
        elif choice == "5":
            undo_delete()
        elif choice == "6":
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")

if __name__ == "__main__":
    menu()
  
