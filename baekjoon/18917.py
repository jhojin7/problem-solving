"""
id: 18917
ac:https://www.acmicpc.net/source/45515786
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
10
1 1
1 2
1 3
4
2 2
1 4
4
1 3
1 1
4
""".strip())

import sys
from operator import xor
input = sys.stdin.readline

XOR, SUM = 0,0

M = int(input())
for _ in range(M):
    query,*x = input().split()
    if query == '3': 
        print(SUM)
    elif query == '4': 
        print(XOR)
    # add
    elif query == '1':
        _x = int(*x)
        SUM += _x
        XOR = xor(XOR,_x)
    # remove
    elif query == '2':
        _x = int(*x)
        SUM -= _x
        XOR = xor(XOR,_x)