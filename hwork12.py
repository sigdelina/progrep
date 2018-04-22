import os
import re

def find_files():
    names = []
    find = os.listdir()
    dirpath = '.'
    for elements in find:
        if os.path.isfile(os.path.join(dirpath, elements)):
            names.append(elements)
    return names

def work(names):
    right = []
    for files in names:
        search = re.search('\d', files)
        if not search:
            right.append(files)
    return right

def final_work(right):
    if right == []:
        print("Файлов без цифр в названии нет")
        exit(0)
    else:
        a = "Количество файлов без цифр в названии: " + str(len(right))
        return a
    
def count2(right):
    symbols = []
    for words in right:
        if words not in symbols:
            symbols.append(words)
    if symbols == []:
        print("Файлов без цифр в названии нет")
        exit(0)
    else:
        a = "Список файлов и папок без повторов:\n" + "\n".join(symbols)
        return a
    
def main():
    find = find_files()
    working = work(find)
    final = final_work(working)
    counting2 = count2(working)
    print(final, '\n')
    print(counting2)

main()
