import re

#2 вариант
#Берлин — Википедия.html
#Санкт-Петербург — Википедия.html

wiki_name = input('Введите название файла,чтобы узнать часовой пояс города: ')

def make_file():
    if wiki_name == '':
        print('такого файла не существует')
        exit(0)
    else:
        file = open(wiki_name, encoding='utf-8')
        file = file.read()
        return file

def city_name(file):
    name = re.search(r'<title>([А-Я][A-Яа-я]+)(.?[А-Я][A-Яа-я]+)* — Википедия</title>', file, re.DOTALL)
    if name is None:
        print("На странице нет названия города")
        exit(0)
    else:
        if name[2] is None:
            name = name[1]
        else:
            name = name[1] + name[2]
    return str(name)
    
def city_time(file):
    time = re.search(r'(UTC\d|UTC[+-−]\d+)(.*(UTC\d|UTC[+-−]\d+))', file, re.DOTALL)
    if time is None:
        print("Время для данного города не указано")
        exit(0)
    return time

def final_time(time):
    if time[3] == time[1]:
        time = "часовой пояс:" + time[1]
    else:
        time = "зимний часовой пояс: " + time[1] + ", летний часовой пояс: " + time[3]
    return str(time)

def read_file(name, time_z):
    written = name + " - " + time_z
    with open("text.txt", "w", encoding = "utf-8") as f:
        f.write(written)
    with open("text.txt", "r", encoding = "utf-8") as f:
        return f.read()
    
file = make_file()
name = city_name(file)
time = city_time(file)
time_z = final_time(time)
read = read_file(name, time_z)
print(read)
