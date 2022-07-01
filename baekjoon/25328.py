"""
id: 25328
ac:https://www.acmicpc.net/source/45345732
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
abc
acde
cde
2
""".strip())

import sys, itertools
input = sys.stdin.readline

X = input().strip()
Y = input().strip()
Z = input().strip()
k = int(input())
# print(X,Y,Z,k)
ans = set()
combx = set(itertools.combinations(X,k))
comby = set(itertools.combinations(Y,k))
combz = set(itertools.combinations(Z,k))
# print(combx,comby,combz)

ans = combx.intersection(comby)
ans.update(comby.intersection(combz))
ans.update(combz.intersection(combx))

if len(ans) == 0:
    print("-1")
else:
    for x in sorted(ans):
        print(''.join(x))
        # print(x)

    