from app.manager import add_password, get_password


def show_menu():
    print("\n🔐 Password Manager")
    print("1. Add new password")
    print("2. Get password")
    print("3. Exit")


def main():
    master_password = input("Enter master password: ")

    while True:
        show_menu()
        choice = input("Choose option (1/2/3): ").strip()

        if choice == "1":
            service = input("Service name: ")
            username = input("Username: ")
            password = input("Password: ")

            add_password(service, username, password, master_password)
            print("✅ Password saved successfully!")

        elif choice == "2":
            service = input("Service name: ")

            try:
                username, password = get_password(service, master_password)
                print(f"👤 Username: {username}")
                print(f"🔑 Password: {password}")
            except ValueError:
                print("❌ Service not found!")

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid option. Try again.")


if __name__ == "__main__":
    main()
