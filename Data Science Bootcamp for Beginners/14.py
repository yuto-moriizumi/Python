import math
values = [16, 14, 7, 151, 170, -105, 40, -14, -7, 128, 40, 15, 92, 28, 6, 122, 98, 6, 132, 15, 50, -3, 36, 38, 48, 34, 45, 14, 11, 14, 23, 22, 41, 159, 94, 116, 16, 125, 143, 104, 10, 33, -6, 156, 31, 5, 6, 18, 26, 128, 122, 19, 8, 22, 17, 92, 25, 34, 123, 23, 143, -31, 149, 28, -1, 107, 20, 26, 11, 10, 131, 67, 47, 11, 54, 142, 2, 117, -111, 46, 26, -9, 123, 155, 69, -5, 156, 87, 122, 150, 103, 25, 25, -63, 109, 66, 36, 118, 13, 17, 30, 122, 22, 167, 144, 69, 132, 149, 25, 145, 6, 137, 5, -12, 21, 152, 147, 22, 124, 10, 144, 93, 13, 52, 9, 110, 122, 157, 28, -65, 108, 144, 27, 137, 111, 118, 23, 123, 155, 156, 115, 70, 171, 122, 8, 14, 32, 2, -10,
          156, 12, 11, 22, 15, 45, 18, 139, -35, 132, 120, 145, 24, -1, 7, 24, 26, -37, 155, -35, 30, 129, -19, 25, 28, 13, 31, -66, 31, 147, 31, -37, 19, 24, 143, 13, 23, 176, 139, -31, 40, 7, 174, 28, 148, 152, 152, 29, 20, 23, 163, 32, 152, 157, 36, 21, 114, 24, 148, 1, 33, -2, 101, 131, 36, 147, 13, 146, 129, 27, 2, 116, 130, 7, 47, 71, 62, 43, 14, 119, 41, 118, 177, 103, 18, 141, 135, 96, 113, 128, 52, 17, 5, 11, 49, -19, -80, 28, 15, 160, 28, 51, 143, 29, 149, 6, 43, 12, 93, 104, 14, 36, 9, 13, 43, 2, 0, 13, 13, 66, 111, 37, 8, 170, -91, 160, 22, 44, -42, -22, 18, 180, 135, 126, 142, 119, 17, 139, 197, 1, -14, 154, 136, -35, 20, -13, 127, 73, 58, 42, 0]


def mean(l):
    if len(l) == 0:
        return None
    return sum(l) / len(l)


def var(l):
    if len(l) == 0:
        return None
    m = mean(l)
    return sum([(i - m) ** 2 for i in l])/len(l)


def std(l):
    if len(l) == 0:
        return None
    return math.sqrt(var(l))


print("標準偏差", std(values))
