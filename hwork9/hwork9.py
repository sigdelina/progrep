#деепричастия: нашедши, найдя. причастия: нашедший, найденный, найдённый. инфинитив: найти, найтись.
#будущее время: найду(сь), найдешь(ся), найдет(ся), найдем(ся), найдете(сь), найдут(ся)
#прошедшее время: нашел(ся), нашла(сь), нашло(сь), нашли(сь)

import re

print("2 вариант.\n\nНайденные слова: ")

def text():
    symbols = [".", ",", "«", "\t", "\n", "\r", "»", "!", "?", "\"", '–', ", ", ". ", " - ", "...", ":", ";", "(", ")", "1", "2", "3", "4", "5","6", "7", "8", "9", "0", "^", "{", "}", ">", "<", "/", "|", "%", "@", "#", "№", "$"]
    text = open("hemi.txt", encoding = "utf-8")
    text = text.read()
    for char in symbols:
        text = text.replace(char, "").lower()
    return text
    
# так как из задания не очень понятно, надо ли вводить название файла, а не автоматически прочитывать его, то прикрепляю фрагмент такой программы:
#def name():
    #ch_file = input("Введите название файла: ")
    #if name_f == '':
    #    print("no name")
    #    exit(0)
    #else:
    #    return name_f
    
##def text(name_f):
##    symbols = [".", ",", "«", "»", "\t", "\n", "\r", "!", "?", "\"", '–', ", ", ". ", " - ", "...", ":", ";", "(", ")", "1", "2", "3", "4", "5","6", "7", "8", "9", "0", "^", "{", "}", ">", "<", "/", "|", "%", "@", "#", "№", "$"]
##    text = open(name_f, encoding = "utf-8")
##    text = text.read()
##    for char in symbols:
##        text = text.replace(char, "").lower()
##    return text
    
def find_word(text):
    words = []
    match = re.findall('найт[ис]*ь*\w*|найд[её]н*н*[ыао]*\w*|найдя|нашедш[иае]*[йяе]*\w*|наш[её]лс*я*\w*|найд[еёу][сштм]*[сье]*\w*|нашл[иоа][яс]*\w*', text) 
    for word in match:
        if word not in words:
            words.append(word)
    if words == []:
        print("В тексте нет таких слов")
        exit(0)
    else:
        for word in words:
            print(word, end = ' ')
        return " "
    
#закомментированы фрагемнты для программы с введением названия файла: 
#name_f = name()
#w_word = text(name_f)
w_word = text()
find_words = find_word(w_word)
print(find_words)
