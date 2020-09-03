from collections import Counter


def count_char(s):
    return dict(Counter(s))


print(count_char("I have a pen"))
