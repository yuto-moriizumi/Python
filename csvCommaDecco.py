out = []
while True:
    i = input()
    if i == "end":
        break
    out.append(i.replace(',', '","'))
f = open('output.txt', mode='w')
for i in out:
    f.write('"'+i+'"\n')
    print('"'+i+'"')
