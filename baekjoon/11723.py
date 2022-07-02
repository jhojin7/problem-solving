"""
id: 11723
title:집합
ac: https://www.acmicpc.net/source/45393035
"""
# pypy x python3 v
import sys
from io import StringIO
sys.stdin = StringIO("""
""".strip())

import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
    command = input().split()
    x = -1
    if len(command) == 2:
        x = int(command.pop())
    command = command.pop()
    # print(">>",command, x)

    if command == "add":
        S.add(x)
    elif command == "remove":
        S.discard(x)
    elif command == "check":
        if x in S: print(1)
        else: print(0)
    elif command == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif command == "all":
        S = set(range(1,21))
    elif command == "empty":
        S = set()
    # print(S)