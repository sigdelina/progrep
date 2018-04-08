#1
import re

def make_file():
    wiki_name = input('Введите название файла: ')
    if wiki_name == '':
        print('такого файла не существует')
        exit(0)
    else:
        file = open(wiki_name, encoding='utf-8')
        file = file.read()
        return file

from itertools import groupby

def find(file):
    surn = []
    surn_2 = []
    name = re.findall('дзе,', file, re.DOTALL)
    name_2 = re.findall('швили,', file, re.DOTALL)
    for word in name:
        surn.append(word)
    for word_2 in name_2:
        surn_2.append(word_2)
    count = str(len(surn)) + " " + str(len(surn_2))
    count = count.split(" ")
    return count

def counter(count):
    if int(count[0]) > int(count[1]):
        return "с фамилией -дзе людей больше в", int(count[0])/int(count[1])
    else:
        return "с фамилией -швили людей больше в", int(count[1])/int(count[1])
##1.1
def find_2(file):
    surn = []
    name = re.findall('ия,', file, re.DOTALL)
    for word in name:
        surn.append(word)
    count = str(len(surn))
    return " с фамилией -ия", count

file = make_file()
search = find(file)
max_f = counter(search)
search_2 = find_2(file)
print(max_f,"\n", search_2)


