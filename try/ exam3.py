import re

def file():
    f = open('karenina.xml', encoding='utf-8')
    f = f.read()
    return f

def sush(f):
    a = re.findall(r'<w><ana.*/>(\w+)</w>(.*)\n<w><ana.*/>(\w+)</w>(.*)\n<w><ana.*/>(\w+)</w>.*\n<.*<ana.*gr="S,.*=твор.*".*/>(\w+)</w>(.*)\n<w><ana.*/>(\w+)</w>(.*)\n<w><ana.*/>(\w+)</w>(.*)\n<w><ana.*/>(\w+)</w>(.*)\n', f)
    f = open("text2.txt", "w", encoding = "utf-8")
    for b in a:
        w = b[0] + b[1] + b[2]+ b[3] + b[4] + '\t' +b[5] + b[6] + '\t' + b[7] + b[8] + b[9] + ' ' + b[10] + b[11] + b[12] + '\n'
        file = f.write(w)
    return ' ЗАПИСАНО!'
    
def main():
    f = file()
    sus = sush(f)
    print(sus)
    
main()
