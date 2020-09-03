from operator import itemgetter
fileStr = "population-abstract2010-2015.csv"
f = open(fileStr, 'r', encoding='utf-8')
csv = [i.split(",") for i in f.readlines()]
ans = dict()
for i in csv[1:]:
    kenmei = i[csv[0].index('area_name')]
    pop2015 = i[csv[0].index('population2015')]
    pop2010 = i[csv[0].index('population2010')]
    ans[kenmei] = abs(int(pop2015) - int(pop2010))
ans = list(ans.items())
ans.sort(key=itemgetter(1), reverse=True)
for i in range(len(ans)):
    print(str(i+1)+'位:'+ans[i][0]+'('+str(ans[i][1])+'人)')

outputFileStr = "10.tsv"
f = open(outputFileStr, "w", encoding="utf-8")
for i in ans:
    f.write(i[0]+","+str(i[1])+"\n")
f.close()
