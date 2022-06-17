"""
id: 11399
title:atm
ac:https://www.acmicpc.net/source/44666795 
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
5
3 1 4 3 2
""".strip())

N = int(input())
people = list(map(int,input().split()))
people.sort()
# print(people)
sum, _sum = 0, 0
for i in range(N):
    sum += _sum + people[i]
    _sum += people[i]
print(sum)
