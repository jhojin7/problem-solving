"""
id: 15652
title:N과M(4)
ac:https://www.acmicpc.net/source/45054809
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
8 2
""".strip())

def dfs(visited:list, idx:int):
    # print(visited)
    if len(visited) == M:
        if visited not in ans:
            ans.append(visited)
        return
    # for n in arr:
    for i in range(idx, len(arr)):
        dfs(visited+[arr[i]],i)

N,M = map(int,input().split())
arr = list(range(1,N+1))
ans = []
dfs([],0)
for l in ans: print(*l,sep=' ')