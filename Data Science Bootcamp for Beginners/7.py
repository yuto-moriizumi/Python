fileStr = "population-abstract2010-2015.csv"
f = open(fileStr, 'r', encoding='utf-8')
for i in f.readlines():
    print(i, end='')
