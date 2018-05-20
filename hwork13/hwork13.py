import os
import re

# До конца не было понятно, что требудется.
# Могут ли быть в названии папки неалфавитные символы (подчеркивания и т.д.)?
# "сколько в дереве папок с полностью кириллическими названиями"
# - поэтому программа находит папки c названиями ТОЛЬКО из кириллических символов, в название программы может быть пробел. 

def find_dirs():
    dirs_list = []
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        for dir_names in dirs:
            dirs_names = re.findall('^[А-Яа-яЁё\s]+$', dir_names) 
            if len(set(dirs_names)) == len(dirs_names):
                dirs_list.append(dirs_names)
    return dirs_list

def dir_list(dirs_list):
    count = []
    for dirs in dirs_list:
        if dirs != []:
            count.append(dirs)
    return len(count)

def main():
    general = find_dirs()
    counting = dir_list(general)
    print("В дереве папок с полностью киррилическими названиями", counting, "штуки.")
    
main()
