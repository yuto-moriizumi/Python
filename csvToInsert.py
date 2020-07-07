print("テーブル名を入力してください")
table = input()
#print("カラム数を入力してください")
#colum = int(input())
print("csvデータを張り付けてね")
mail=[]
while(True):
    i = input()
    if(i=="end"):
        break
    test=i.split(",")
    test2='"'
    for n in range(len(test[0])):
        test2.append(test[0][n])
    mail.append()

for i in mail:
    print("INSERT INTO " + table + " VALUES (" + i +");")
