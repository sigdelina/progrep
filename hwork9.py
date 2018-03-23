#деепричастия: нашедши, найдя. причастия: нашедший, найденный, найдённый. инфинитив: найти, найтись.
#будущее время: найду(сь), найдешь(ся), найдет(есь), найдем(ся), найдете(сь), найдут(ся)
#прошедшее время: нашел(ся), нашла(сь), нашло(сь), нашли(сь)

import re

print("2 вариант.\n\nНайденные слова: ")

def text():
    symbols = [".", ",", "«", "»", "!", "?", "\"","\r", '–', ", ", ". ", " - ", "...", ":", ";", "(", ")","\t", "\n", "1", "2", "3", "4", "5","6", "7", "8", "9", "0", "^", "{", "}", ">", "<", "/", "|", "%", "@", "#", "№", "$", "\n", "\t"]
    with open("hemi.txt", "r", encoding = "utf-8") as text:
        for lines in text:
            for char in symbols:
                lines = lines.replace(char, "").lower()
            lines = lines.replace("\n", "").replace("\t", "").replace("\r", "")
        return lines
    
def find_word(lines):
    words = []
    for line in lines:
        match = re.findall('найти*[c]*\w+|найд[её]нн*[ыао]*\w+|нашедш[иае]*[йяе]*\w+|найдя|найд[уеё]*[сштм]*[сье]*[ся]*[яь]*\w+|наш[еёл]*ся\w+|нашл[иоа]*[яс]*\w+', lines) 
    for word in match:
        if word not in words:
            words.append(word)
    if words == []:
        print("В тексте нет таких слов")
        exit(0)
    else:
        for word in words:
            print(word, end = ' ')
        return word
    
w_word = text()
find_words = find_word(w_word)
print(find_words)
