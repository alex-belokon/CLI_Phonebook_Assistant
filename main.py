def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please be more attentive!"

    return wrapper

@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return f"You've added {name} with phone {phone} to your Phonebook"
    
@input_error
def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"New phone number for {name} is {phone}"
    else:
        return f"Can't find {name} in the Phonebook. Please be more attentive!"

@input_error
def get_phone(contacts, name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        return f"Can't find {name} in the Phonebook. Please be more attentive!"

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split()
            print(add_contact(contacts, name, phone))
        elif command.startswith("change"):
            _, name, phone = command.split()
            print(change_contact(contacts, name, phone))
        elif command.startswith("phone"):
            _, name = command.split()
            print(get_phone(contacts, name))
        elif command == "show all":
            show_all(contacts)
        elif command in {"good bye", "close", "exit"}:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please be more attentive.")

if __name__ == "__main__":
    main()
    