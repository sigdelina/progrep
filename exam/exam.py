import os
import re
import csv

def file():
    obj = []
    s = []
    path = './news/'
    for root, dirs, files in os.walk(path):
        for f in files:
            file = path + f
            with open(file,'r', encoding='utf=8') as fin:
                fin = fin.readlines()
                for line in fin:
                    find = re.sub('`', '', line)
                    find2 = re.sub('[A-zZ-a]', '', find)
                    find4 = re.sub(r'<w><ana.*</ana>','', find2)
                    find3 = re.sub('<>|?/\\', '', find4)
                #a = find3 + ' ' 
                #print(a)
               # r = re.compile('</ana>(.*)</w>(.*)(<w>),')
                  #  find2 = re.sib('</ana>(.*)</w>(.*)(<w>)', '', find)
              #  print(find2)
                    if find3 != None:
                 #   print()
                  #  print(obj)
                #if find != None:
                        #obj.append(find3)
              #  filename = file(".txt")
                #from pathlib import Path filename = file new_filename = Path(filename).stem + ".txt" 
            #os.path.splitext(file.html)[0]+".txt" 
                        with open("new.txt",'w', encoding='cp1251') as fi:
                            fi.write(find3)
                        print(fi)
   # return fi
  #  return obj, file

#def write_t(obj, file):
   # with open(file,'w', encoding='cp1251') as fin:
    #    fin.write(obj)
     #   return fin
     
def sec():
    obj = []
    slo = {}
    path = './news/'
    for root, dirs, files in os.walk(path):
        for f in files:
            file = path + f
            print(file)
            with open(file,'r', encoding='utf=8') as fin:
                fin = fin.readlines()
            for line in fin:
                find = re.search(r'<w><ana lex="([A-Я][а-я]+)"', line)
                if find != None:
                    obj.append(find[1])
    for word in obj:
        if word in slo:
            slo[word] += 1
        else:
            slo[word] = 1
    print(slo)
    return slo

def cr_csv(slo):
    sl = []
    for word in sorted(slo.keys()):
        sl.append(word + '\t' + str(slo[word]))
    return sl

def pri(sl):
    with open('clovar.csv', 'w', encoding='utf-8', newline="") as file:
        columns = ['имя', 'количество']
        for line in sl:
            line = '\n'.join(sl)
            file.write(line + "\n")
    return file
   
def main():
    d = file()
    second = sec()
    wri = cr_csv(second)
    fo = pri(wri)

    print(fo)

main()
