import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def add_contact(contacts, name, phone_number, email):
    contacts[name] = {'phone_number': phone_number, 'email': email}
    save_contacts(contacts)

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone_number']}")
            print(f"Email: {info['email']}")
            print()

def edit_contact(contacts, name, new_phone_number, new_email):
    if name in contacts:
        contacts[name]['phone_number'] = new_phone_number
        contacts[name]['email'] = new_email
        save_contacts(contacts)
        print(f"{name}'s contact information updated.")
    else:
        print(f"{name} not found in contacts.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name}'s contact deleted.")
    else:
        print(f"{name} not found in contacts.")

def main():
    contacts = load_contacts()

    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone_number, email)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            name = input("Enter name to edit: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            edit_contact(contacts, name, new_phone_number, new_email)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()