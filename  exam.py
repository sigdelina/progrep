import re
import collections
import operator

def file():
    f = open('karenina.xml', encoding='utf-8')
    f = f.read()
    return f

def reg(f):
    ana = re.findall('ana', f)
    w = re.findall('<w>', f)
    count = round(len(ana) / len(w), 2)
    return count

def freu(f):
    freq = {}
    gram  = re.findall('gr="([A-Z]*)', f)
    for word in gram:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def slovar(freq):
    f = open("text.txt", "w", encoding = "utf-8")
    for key in sorted(freq.keys()):
        written = "%s\t%s" % (key, freq[key])
        file = f.write(written + '\n')
    return f.close()

def sush(f):
    first = []
    line = f.split('\n')
    print(line)
##    for line in f:
##        print(line)
##        a = re.search('<ana lex=".*" gr="S,.*=(.*твор)', line)
##        if a:
##            print(a)
##            b = re.findall(a, '<w>\n(<ana.*\n)*[А-аЯ-я]*\n*</w>')
##            fi = first.append(b)

    
def main():
    f = file()
    r = reg(f)
    freq = freu(f)
    s = slovar(freq)
    sus = sush(f)
    print("среднее количество разборов (тэг ana) на слово (тэг w): ", r, '\n', freq, '\n', sus)
    
main()
