import csv


class Row:

    def __init__(self, table_id, num, reason, status):
        self.table_id = table_id
        self.num = num
        self.reason = reason
        self.status = status

    def __repr__(self):
        return f"{self.table_id}, {self.num}, {self.reason}, {self.status}"

    def __getitem__(self, item):
        cur_str = [self.table_id, self.num, self.reason, self.status]
        return cur_str[item]


class Person(Row):

    def __iter__(self):
        return iter([self.table_id, self.num, self.reason, self.status])


caller_list = []
new_caller_list = []
filename = "data.csv"

print("Исходный список")
with open(filename, 'r', newline='') as stream:
    reader = csv.reader(stream, delimiter=';')
    for row in reader:
        person = Person(*row)
        caller_list.append(person)
        print(person)

field_list = Row(caller_list[0][0], caller_list[0][1], caller_list[0][2], caller_list[0][3])
caller_list.remove(caller_list[0])

print("Введите данные в следующем формате:")
print(field_list[0], field_list[1], field_list[2], field_list[3])
person = input().split()
new_caller_list.append(Person(person[0], person[1], person[2], person[3]))

with open(filename, "w", newline='') as stream:
    writer = csv.writer(stream, delimiter=';')
    writer.writerow(field_list)
    writer.writerows(caller_list)
    writer.writerows(new_caller_list)

print("Новый список")
with open(filename, 'r', newline='') as stream:
    reader = csv.reader(stream, delimiter=";")
    for row in reader:
        person = Person(*row)
        print(person)
