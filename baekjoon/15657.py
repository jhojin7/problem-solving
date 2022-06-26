"""
id: 15657
title:N과M(8)
ac:https://www.acmicpc.net/source/45057117
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
4 4
1 2 3 4
""".strip())

import sys
def dfs(visited:list, idx:int):
    if len(visited) == M:
        ans.append(sorted(visited))
        return
    for i,n in enumerate(arr):
        if i < idx:
            continue
        dfs(visited+[n],i)

N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split())) 
ans = []
dfs([],0)
for l in sorted(ans): 
    for n in l:
        sys.stdout.write(str(n)+' ')
    sys.stdout.write("\n")
    # print(*l,sep=' ')