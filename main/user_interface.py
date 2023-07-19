from db_work import *
import datetime

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
            case "3":
                add_entry(add_menu())


def add_menu():
    add_dict = {"id": "1", "заголовок": "", "тело заметки": "", "дата последней редакции": ""}
    for i in add_dict:
        if i != "id" and i != "дата последней редакции":
            add_dict[i] = check_new_data(i)
    date = datetime.datetime.now()
    add_dict[i] = date.strftime("%d-%m-%Y %H:%M")
    return add_dict
