glas = 'АаЕеЁёИиОоУуЭэЮюЫыЯя'
word = str(input("add word or phrase:"))
if word == '':
    print("no word((((")
else:
    for char in glas:
        word = word.replace(char, char + 'c' + char)
    print(word)
