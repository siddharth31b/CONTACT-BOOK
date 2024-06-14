contacts = {}

while True:
    print("\nContact Management")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    option = input("\nChoose an option: ")

    if option == "1":
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email: ")
        address = input("Enter the address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact added.")
    elif option == "2":
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
    elif option == "3":
        search = input("Enter the name or phone number: ")
        for name, details in contacts.items():
            if search in [name, details['Phone']]:
                print(f"\nName: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                break
        else:
            print("Contact not found.")
    elif option == "4":
        name = input("Enter the name of the contact to update: ")
        if name in contacts:
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif option == "5":
        name = input("Enter the name of the contact to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif option == "6":
        break
    else:
        print("Invalid option. Please choose a valid option.")