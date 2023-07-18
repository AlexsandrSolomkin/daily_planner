from os import path
import csv

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
        print("The database is not connected!")


def print_all():
    for_output = [" ".join(k.values()) for k in all_data]
    print(*for_output, sep="\n", end=f"\n{'-' * 20}\n\n")
