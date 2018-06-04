import re

def read_file():
    elements = ';:()\n\t\r%$#@/\<>«»\",–_{}[]'
    with open('hemi.txt', encoding='utf-8') as text_sen:
        text = text_sen.read()
        for char in elements:
            text = text.replace(char, '')
    return text

def text_file(text):
    sent = re.compile(r'[.|!|?|…]')
    result = [line.strip() for line in sent.split(text)]
    return result

def findings(result):
    sent = []
    for lines in result:
        line = lines.split(' ')
        if len(line) >= 10:
            sent.append(lines)
    return sent

def sentences(sent):
    a = []
    for sen in sent:
        words = re.findall('[А-Я]\w+', sen)
        for el in words:
            print(el)
    return ''
    

def main():
    file = read_file()
    text = text_file(file)
    find = findings(text)
    sent = sentences(find)
    print(sent)

main()
