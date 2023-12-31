from os import path
import csv
import datetime

all_data = {}
last_id = 0
name_db = "main/data_csv/daily_planner.csv"


def read_all():
    global all_data, last_id

    print(name_db)
    if path.exists(name_db):
        with open(name_db, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_data = [i for i in csv_reader]
            last_id = all_data[-1]["id"]
            return all_data
    else:
        print("База данных не подключена!")
        

def print_all():
    for_output = [" ".join(k.values()) for k in all_data]
    print(*for_output, sep="\n", end=f"\n{'-' * 20}\n\n")


def add_entry(data):
    global last_id

    if all(data.values()) and matching_rec(data, all_data):
        last_id = int(last_id) + 1
        data["id"] = last_id

        with open(name_db, "a", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "заголовок", "тело заметки", "дата последней редакции"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            print("Заметка добавлена")
    else:
        print("В базе данных уже существует данная заметка")


def matching_rec(new_entry: dict, all_info):
    value = list(new_entry.values())[1:]
    all_values = [list(k.values())[1:] for k in all_info]
    return value not in all_values


def check_new_data(num):
    answer = input(f"Введите {num}: ")
    while True:
        if num in "заголовок тело заметки":
            if answer.isalpha():
                break
        
        answer = input(f"Данные неверны!\n"
                       f"Используйте только буквы"
                       f" из алфавита.\n"
                       f"Введите {num}: ")
    return answer


def del_entry(id_del):
    global all_data

    id_cand = find_entry(id_del, all_data)
    if id_cand:

        if id_del in id_cand:
            all_data = [k for k in all_data if k["id"] != id_del]
            with open(name_db, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "заголовок", "тело заметки", "дата последней редакции"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)
                print("Данные удалены\n")
        else:
            print("Id не найден.\n")


def find_entry(data_find, all_info):
    candidates = [" ".join(i.values()) for i in all_info if data_find in i.values()]
    if candidates:
        print(*candidates, sep="\n", end="\n\n")
        return [n[0] for n in candidates]
    else:
        print("Данные не были найдены\n")
        return 0

def edit_entry(data_change, time, id_change):
    global all_data
    key, value = data_change

    if find_entry(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                v[key] = value
                v["дата последней редакции"] = time
                all_data[i] = v
                

        with open(name_db, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "заголовок", "тело заметки", "дата последней редакции"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)
            print("Данные отредактированы\n")
    else:
        print("Данные не были найдены.\n")
