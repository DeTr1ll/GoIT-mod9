def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"ERROR! Enter user name"
        except ValueError as e:
            return f"ERROR! Give me name and phone please"
        except IndexError as e:
            return f"ERROR! Invalid command format"
        except Exception as e:
            return f"ERROR! Something went wrong"

    return wrapper


@input_error
def hello():
    return "How can I help you?"


@input_error
def show_all(contacts):
    if not contacts:
        raise ValueError()

    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()


@input_error
def add_contact(contacts, name, phone):
    if len(name) == 0 or not phone.isdigit():
        raise ValueError()

    contacts[name] = phone
    return f"Contact {name} added with phone {phone}"


@input_error
def change_phone(contacts, name, phone):
    if len(name) == 0 or not phone.isdigit():
        raise ValueError()

    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated to {phone}"
    else:
        raise KeyError()


@input_error
def get_phone(contacts, name):
    if len(name) == 0:
        raise ValueError()

    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
        raise KeyError()


@input_error
def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ").lower()
        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        elif user_input == "hello":
            print(hello())
        elif user_input.startswith("add"):
            args = user_input.split(maxsplit=2)
            if len(args) == 3:
                _, name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command format. Please try again.")
        elif user_input.startswith("change"):
            args = user_input.split(maxsplit=2)
            if len(args) == 3:
                _, name, phone = args
                print(change_phone(contacts, name, phone))
            else:
                print("Invalid command format. Please try again.")
        elif user_input.startswith("phone"):
            _, name = user_input.split(maxsplit=1)
            print(get_phone(contacts, name))
        elif user_input == "show all":
            print(show_all(contacts))
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()