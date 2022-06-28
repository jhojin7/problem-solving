"""
id: 25304
title:영수증
ac:https://www.acmicpc.net/source/45159999
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
250000
4
20000 5
30000 2
10000 6
5000 8
""".strip())

X = int(input())
N = int(input())
total = 0
for _ in range(N):
    a,b = map(int,input().split())
    total += a*b
if total == X: print("Yes")
else: print("No")