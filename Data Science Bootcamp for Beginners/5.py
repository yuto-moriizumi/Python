from collections import Counter
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.split()
ans = [i[0] for i in Counter(s).most_common()]
print(ans)
