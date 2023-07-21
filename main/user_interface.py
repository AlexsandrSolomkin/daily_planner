from db_work import *
import datetime

def menu():
    while True:
        read_all()
        print(f"{'*' * 20}\n\nПриложение заметки\n\n{'*' * 20}")
        actions = input("1. Показать все заметки\n"
                        "2. Добавить заметку\n"
                        "3. Редактировать заметку\n"
                        "4. Удалить заметку\n"
                        "5. Выйти\n")
        match actions:
            case "1":
                print_all()
            case "2":
                add_entry(add_menu())
            case "3":
                print_all()
                id_change = input(f"Введите id: ")

                if find_entry(id_change, read_all()) and (answer := edit_menu()):

                    date = datetime.datetime.now()
                    date = date.strftime("%d-%m-%Y %H:%M")

                    edit_entry(answer, date, id_change)

            case "4":
                id_d = input(f"Введите id: ")
                del_entry(id_d)
            case "5":
                print("Пока! Увидимся дорогой пользователь! ;)")
                break
            case _:
                print("Данные не распознаны, повторите ввод.")


def add_menu():
    add_dict = {"id": "1", "заголовок": "", "тело заметки": "", "дата последней редакции": ""}
    for i in add_dict:
        if i != "id" and i != "дата последней редакции":
            add_dict[i] = check_new_data(i)
    date = datetime.datetime.now()
    add_dict[i] = date.strftime("%d-%m-%Y %H:%M")
    return add_dict


def edit_menu():
    add_dict = {"1": "заголовок", "2": "тело заметки", "3": "дата последней редакции"}
    while True:
        print("\nРедактировать:")
        change = input("1. заголовок\n"
                       "2. тело заметки\n"
                       "4. выход\n")

        match change:
            case "1" | "2":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "4":
                return 0
            case _:
                print("Данные не распознаны, повторите ввод.")

