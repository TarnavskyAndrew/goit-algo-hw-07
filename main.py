# bot_assistant
from colorama import Fore
from models.AddressBook import AddressBook
from handlers.commands import (
    add_contact,
    change_contact,
    show_phone,
    show_all_contacts,
    add_birthday,
    show_birthday,
    birthdays
)

def parse_input(user_input):           
    parts = user_input.strip().split()
    if not parts:
        return "", []        # якщо користувач введе пусте значення
    cmd, *args = parts
    return cmd.lower(), args   # повертаємо команду та аргументи як список


def main():
    book = AddressBook()
    # FILENAME = "./TASKs/task_4/bot_assistant/contacts.txt"
    # contacts = load_contacts_from_file(FILENAME) 
    print("Welcome to the assistant bot!")
    
    

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if not command:
            print(f"{Fore.YELLOW} Empty input. Type a command like 'hello' or 'add'.{Fore.RESET}")   
            continue  # користувач нічого не ввів - пропускаємо

        if command in ["close", "exit"]:        # exit або close – завершити роботу бота.
            # save_contacts_to_file(FILENAME, contacts)
            print(f"{Fore.GREEN}Goodbye, have a nice day!{Fore.RESET}")            
            break
        
        
        elif command == "hello":                # hello – вітання від бота.
            print("How can I help you?")            
            
        elif command == "add":                  # add [ім'я] [номер] — додати новий контакт або номер до наявного.
            print(add_contact(args, book))
            
        elif command == "change":               # change [ім'я] [старий_номер] [новий_номер] — щоб змінити номер телефону для вказаного контакту.
            print(change_contact(args, book))                         

        elif command == "phone":                # phone [ім'я] — щоб показати всі номери телефону для вказаного контакту.
            print(show_phone(args, book))

        elif command == "all":                  # all — показати всі контакти з номерами та датами привітання (якщо є).
            print(show_all_contacts(book))
    
        elif command == "add-birthday":         # add-birthday [ім'я] [DD.MM.YYYY] – додати дату народження до контакту.
            print(add_birthday(args, book))

        elif command == "show-birthday":        # show-birthday [ім'я] – показати дату народження вказаного контакту.
            print(show_birthday(args, book))

        elif command == "birthdays":            # birthdays - показати список контактів, яких потрібно привітати по днях на наступному тижні.
            print(birthdays(args, book))          

                    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()