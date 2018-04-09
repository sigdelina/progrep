#2вариант

#осталось не очень понятным, какие строки считать, поэтому в программе приведено решение для определения количества всех написанных строк в файле
#однако, если я все-таки поняла не совсем так, что в функции find есть регулярное выражение, которое ищет другие строки, для этого его нужно раскомментировать

import re
import collections

def make_file():
    file = open("island.xml", encoding="utf-8")
    file = file.read()
    return file

def find(file):
    counti = re.findall(r'\n', file)
    ##counti = re.findall(r'<w.*', file) #если подразумевается, что строки выглядят как на одной строке - одна словоформа (<w lemma="til" type="ae">Til</w>), тогда регулярное выражение будет выглядить так
    return counti

def count(counti):
    n_file = open("new_island.txt", "w", encoding="utf-8")
    f = n_file.write(str(len(counti) + 1))
    return f

##2

def clovar(file):
    find = re.findall('lemma=".*" type="(.*)"', file)
    return find

def slova(find):
    freq = {}
    counter = collections.Counter(find)
    freq.update(counter)
    return freq

def slova_file(freq):
    b = list(freq.keys())
    print(b)
    with open("new_slovar_file.txt", "w", encoding="utf-8") as s_file:
        s_file.write(str(b))
    return s_file

def main():
    open_f = make_file()
    finding = find(open_f)
    counting = count(finding)
    slov = clovar(open_f)
    slovar = slova(slov)
    file_s = slova_file(slovar)
    print("Узайте количество строк в файле")
    print("Узнайте формы в файле")
main()
