mail = []
while(True):
    i = input()
    if(i == "end"):
        break
    mail.append(i)


for i in mail:
    print(i, end=";")
