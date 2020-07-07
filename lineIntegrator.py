data = []
while (True):
    s = input().replace('\n', '').replace('。', '。\n')
    if (s == 'end'):
        break
    data.append(s)
print(*data, sep='')
