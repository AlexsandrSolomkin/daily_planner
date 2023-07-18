from db_work import *

def menu():
    while True:
        read_all()
        print(f"{'*' * 20}\n\nПриложение заметки\n\n{'*' * 20}")
        actions = input("1. Показать все заметки\n"
                        "3. Добавить заметку\n"
                        "4. Редактировать заметку\n"
                        "5. Удалить заметку\n"
                        "7. Выйти\n")
        match actions:
            case "1":
                print_all()
