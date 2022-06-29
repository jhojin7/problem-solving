"""
id: 1697
title:숨바꼭질
ac:https://www.acmicpc.net/source/45200556
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
3 100000
""".strip())

import collections

def bfs(src,dest):
    queue = collections.deque([(0,src)])
    visited = set()
    cnt = 0
    while queue:
        cnt,cur = queue.popleft()
        if not 0<= cur <= 100000: continue
        if cur in visited: continue
        # print(cnt,cur)
        visited.add(cur)
        if cur==dest: 
            # print(visited)
            return cnt
        
        to_add = []
        if 0<= cur*2 <= 100000:
            to_add.append((cnt+1,cur*2))
        if 0<= cur-1 <= 100000:
            to_add.append((cnt+1,cur-1))
        if 0<= cur+1 <= 100000:
            to_add.append((cnt+1,cur+1))
        queue.extend(to_add)

src,dest = map(int,input().split())
print(bfs(src,dest))