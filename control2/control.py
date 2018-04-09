#2вариант

import re

def make_file():
    file = open("island.xml", encoding="utf-8")
    file = file.read()
    return file

def find(file):
    counti = re.findall(r'\n', file)
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
