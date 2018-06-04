import re

def read_file():
    elements = ';:()\n\t\r%$#@/\<>«»\",–_—{}[]'
    with open('cheh.txt', encoding='utf-8') as text_sen:
        text = text_sen.read()
        for char in elements:
            text = text.replace(char, '')
    return text

def text_file(text):
    sntc = re.compile(r'[.|!|?|…]')
    result = [line.strip() for line in sntc.split(text)]
    return result

def findings(result):
    sent = []
    for lines in result:
        line = lines.split(' ')
        if len(line) >= 10: #находит предложение от 10 слов, если такое возможно согласно заданию
            sent.append(lines)
    return sent

def sentences(sent):
    a = []
    for sen in sent:
        print('Предложение: \n\t', sen, '\nCлова для преждожения с заглавной буквы:') #вывожу с предложениями, так как в задании указано вывести слова для предложения
        words = re.findall('[А-Я]\w*', sen)
        for el in words:
            print('\t', el)
    return ''
    

def main():
    file = read_file()
    text = text_file(file)
    find = findings(text)
    sent = sentences(find)
    print(sent)

main()
