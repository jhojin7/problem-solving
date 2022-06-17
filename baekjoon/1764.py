"""
id: 1764
title:듣보잡
ac: https://www.acmicpc.net/source/44666086
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
3 4
ohhenrie
charlie
baesangwook
obama
clinton
ohhenrie
baesangwook
""".strip())

N,M = map(int,input().split())
set_N = set()
set_M = set()
for _ in range(N):
    set_N.add(input())
for _ in range(M):
    set_M.add(input())

ans = sorted(list(set_N.intersection(set_M)))
print(len(ans))
while ans:
    print(ans.pop(0))

