"""
id: 3344
ac:https://www.acmicpc.net/source/45578157
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
99
""".strip())

import sys
input = sys.stdin.readline
# explicit solutions to nqueens

n = int(input()) # 8, 26, 213, 2012, 99991, 99999
evens,odds = [],[]

for x in range(1,n+1):
    if x%2==0: evens.append(x)
    elif x%2==1: odds.append(x)

if n%6 == 2:
    i1 = odds.index(1)
    i2 = odds.index(3)
    odds[i1],odds[i2] = odds[i2],odds[i1]
    five = odds.pop(odds.index(5))
    odds.append(five)

if n%6 == 3:
    two = evens.pop(evens.index(2))
    evens.append(two)

    one = odds.pop(odds.index(1))
    three = odds.pop(odds.index(3))
    odds.append(one)
    odds.append(three)

# print(*(evens+odds),sep="\n")
print(evens+odds)