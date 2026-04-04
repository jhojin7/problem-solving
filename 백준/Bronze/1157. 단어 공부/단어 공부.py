from collections import Counter

s = input().lower()
cntr = Counter([c for c in s])
n = max(cntr.values())
c = [k for k, v in cntr.items() if v == n]

if len(c) > 1 or len(c) < 1:
    print("?")
else:
    print(c[0].upper())
