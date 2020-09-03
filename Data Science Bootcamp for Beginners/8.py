fileStr = "population-abstract2010-2015.csv"
f = open(fileStr, 'r', encoding='utf-8')
csv = [i.split(",") for i in f.readlines()]
ans = dict()
for i in csv[1:]:
    kenmei = i[csv[0].index('area_name')]
    pop2015 = i[csv[0].index('population2015')]
    pop2010 = i[csv[0].index('population2010')]
    ans[kenmei] = int(pop2015)-int(pop2010)
print(ans)
