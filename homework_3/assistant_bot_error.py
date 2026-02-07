#Парсування тексту

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#Декоратор для обробки помилок при додаванні та зміні контактів

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Write name and number.'
        except IndexError:
            return 'Command without arguments.'
        except KeyError:
            return 'Incorrect key.'

    return inner

#Додавання контакту

@input_error
def add_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    

#Зміна номеру контакту

@input_error
def change_contact(args, contacts):
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return 'Contact changed.'
        

#Вивід номеру телефону за ім'ям контакту

@input_error
def show_phone(args, contacts):
        name = args[0]
        if name in contacts:
            return f'Number: {contacts.get(name)}'


#Вивід усіх контактів та їх номерів телефонів

@input_error
def show_all(args, contacts):
    if len(args) > 0:
        return 'Unknown symbols after command.'
    
    return f'Contacts dict: {contacts}'
    
#Основна функція

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'show':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()