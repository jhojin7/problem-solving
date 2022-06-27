"""
id: 15666
title:N과M(12)
ac:https://www.acmicpc.net/source/45081467
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
8 8
8 7 6 5 4 3 2 1
""".strip())

import sys
def dfs(visited:list, idx:int):
    if len(visited) == M:
        if visited not in ans:
            ans.append(visited)
        return
    for i,n in enumerate(arr):
        if i < idx: continue
        dfs(sorted(visited+[n]),i)

N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split())) 
ans = []
dfs([],0)

for l in sorted(ans): 
    for n in l:
        sys.stdout.write(str(n)+' ')
    sys.stdout.write("\n")