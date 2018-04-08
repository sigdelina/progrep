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
    
def find(file):
    name_r = re.compile('href=.*title=.[А-Я].*дзе,.[А-Я].* [А-Я].*</a> ')
    name_r_2 = re.compile('href=.*title=.[А-Я].*швили,.[А-Я].* [А-Я].*</a> ')
    name = name_r.findall(file, re.DOTALL)
    name_2 = name_r_2.findall(file, re.DOTALL)
    count = [len(name), len(name_2)]
    return count

def counter(count):
    if int(count[0]) > int(count[1]):
        a = " Людей с фамилией -дзе больше в " + str(round(int(count[0])/int(count[1]), 3))
    else:
        if int(count[0]) == int(count[1]):
            a = " Людей с фамилиями -дзе и -швили одинаковое количество"
        else:
            a = " Людей с фамилией -швили больше в " + str(round(int(count[1])/int(count[1]), 3))
    return a

##1.1
            
def find_2(file):
    name = re.compile('href=.*title=.[А-Я].*ия,.[А-Я].* [А-Я].*</a> ')
    name_1 = name.findall(file, re.DOTALL)
    count = len(name_1)
    a = "Людей с фамилией на -ия " + str(count)
    return a
##2

def find3(file):
    #name = re.compile(r'title=\"(.+?)\">(?:[а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я]+) ([а-яА-я])([а-яА-Я]+(?:(швили)|(дзе)))</a>",r"title=\"\1\">Галактион \2 \3</a>')
    name = re.sub(r"title=\"(.+?)\">(?:[а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я][а-яА-Я]+) ([а-яА-Я]+) ([а-яА-Я]+(?:(швили)|(дзе)))</a>",r"title=\"\1\">Галактион \2 \3</a>",file)
    return name

def rewrite(name, file):
    f = open("new-html.html","w",encoding="utf-8")
    f = f.write(name)
    return f

def main():
    file = make_file()
    search = find(file)
    max_f = counter(search)
    search_2 = find_2(file)
    search_3 = find3(file)
    end = rewrite(search_3, search)
    print(max_f, "\n", search_2, "\n", end)

main()
