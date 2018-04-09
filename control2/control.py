#2вариант

#осталось не очень понятным, какие строки считать, поэтому в программе приведено решение для определения количества всех написанных строк в файле
#однако, если я все-таки поняла не совсем так, что в функции find есть регулярное выражение, которое ищет другие строки, для этого его нужно раскомментировать

import re

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
    f = n_file.write(str(len(counti)))
    return f
        
def main():
    open_f = make_file()
    finding = find(open_f)
    counting = count(finding)
    print("Узайте количество строк в файле")
main()
