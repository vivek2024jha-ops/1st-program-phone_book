
import os

FILE_NAME = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, number = line.strip().split(",")
                contacts[name] = number
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")

def show_menu():
    print("\n--- Phone Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

phone_book = load_contacts()

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        save_contacts(phone_book)
        print(f"Contact {name} added successfully!")

    elif choice == "2":
        if phone_book:
            print("\n--- All Contacts ---")
            for name, number in sorted(phone_book.items()):
                print(f"{name} : {number}")
        else:
            print("No contacts found.")

    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in phone_book:
            print(f"{search_name} : {phone_book[search_name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        del_name = input("Enter name to delete: ")
        if del_name in phone_book:
            del phone_book[del_name]
            save_contacts(phone_book)
            print(f"Contact {del_name} deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        update_name = input("Enter name to update: ")
        if update_name in phone_book:
            new_number = input("Enter new phone number: ")
            phone_book[update_name] = new_number
            save_contacts(phone_book)
            print(f"Contact {update_name} updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Exiting Phone Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-6.")
