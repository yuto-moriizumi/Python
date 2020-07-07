class Data:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def __str__(self):
        return '('+str(self.number)+','+str(self.name)+')'


def printDataArray(array):
    print('[', end='')
    for i in array:
        print(i, end=',')
    print(']')


data = []
print('数字と識別名を半角スペースで区切って入力してください end→ソート開始')
while True:
    i = input()
    if i == 'end':
        break
    i = i.split()
    data.append(Data(int(i[0]), i[1]))
    # data.append(int(i))
printDataArray(data)
heap = []
for i in data:
    heap.append(i)
    i = len(heap)-1
    while(i > 0 and heap[i//2].number > heap[i].number):
        t = heap[i]
        heap[i] = heap[i//2]
        heap[i//2] = t
        i = i//2
printDataArray(heap)
while(len(heap) > 1):
    r = heap[0]
    heap[0] = heap.pop()
    i = 0
    while(i*2 < len(heap)):
        toSwap = i
        if i*2+1 < len(heap) and heap[i].number > heap[i*2+1].number:
            toSwap = i*2+1
        if i*2+2 < len(heap) and heap[toSwap].number > heap[i*2+2].number:
            toSwap = i*2+2
        if i == toSwap:
            break
        t = heap[toSwap]
        heap[toSwap] = heap[i]
        heap[i] = t
        i = toSwap
    print(r)
print(heap.pop())
