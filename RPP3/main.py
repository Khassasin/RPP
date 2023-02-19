import os
import csv
import operator


# Чтение файла и запись в список словарей
def file_reader(file_name):
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        list_of = list(reader)
    return list_of


# Вывод списка
def print_list(list_name):
    for i in list_name:
        print(i)

# Запись новой строки в таблицу
def write_file(file_name):
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        key_list = reader.fieldnames
    with open(file_name, 'a') as file:
        dict_info = {}
        writer = csv.DictWriter(file, key_list, delimiter=';')
        for i in key_list:
            print(i)
            dict_info[i] = input()
        writer.writerow(dict_info)


print("Количество файлов в папке: " + str(len([name for name in os.listdir('.') if os.path.isfile(name)])))

filename = "data.csv"

list_of_dict = file_reader(filename)
print("Исходный список")
print_list(list_of_dict)
new_list = sorted(list_of_dict, key=operator.itemgetter("Номер"))
print("Сортировка по номеру")
print_list(new_list)
new_list = sorted(list_of_dict, key=operator.itemgetter("Причина обращения"))
print("Сортировка по причине обращения")
print_list(new_list)

write_file(filename)

list_of_dict = file_reader(filename)
print("Новый список")
print_list(list_of_dict)
