"""
id: 11659
title:구간합구하기4
ac:https://www.acmicpc.net/source/44682798
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
5 3
5 4 3 2 1
1 3
2 4
5 5
""".strip())

import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0]+[*map(int,sys.stdin.readline().split())]
tmp = 0
for i in range(1,N+1):
    tmp += arr[i]
    arr[i] = tmp
# print(arr)
for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    print(arr[j]-arr[i-1])