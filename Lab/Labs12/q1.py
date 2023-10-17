phone_book = {}

def add_contact(name, number):
    phone_book[name] = number
    print(f"Added {name} with number {number} to the phone book.")

def remove_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Removed {name} from the phone book.")
    else:
        print(f"{name} is not in the phone book.")

# Function to search for a contact in the phone book
def search_contact(name):
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"{name} is not in the phone book.")

# Function to display all contacts in the phone book
def display_contacts():
    print("Phone Book:")
    for name, number in phone_book.items():
        print(f"{name}: {number}")

# Main program loop
while True:
    print("\nPhone Book Menu:")
    print("+. Add Contact")
    print("-. Remove Contact")
    print("f. Search Contact")
    print("p. Display Contacts")
    print("q. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "+":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == "-":
        name = input("Enter name: ")
        remove_contact(name)
    elif choice == "f":
        name = input("Enter name: ")
        search_contact(name)
    elif choice == "p":
        display_contacts()
    elif choice == "q":
        break
    else:
        print("Invalid choice.")

    