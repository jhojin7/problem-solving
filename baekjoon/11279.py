"""
id: 11279
title:최대힙
ac:https://www.acmicpc.net/source/44699258
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
""".strip())

import sys,heapq
N = int(sys.stdin.readline().strip())
pq = []
for _ in range(N):
    x = -int(sys.stdin.readline().strip())
    # x = -int(input()) # invert val for maxheap
    if x == 0:
        try: print(-heapq.heappop(pq))
        except IndexError: print(0)
    else:
        heapq.heappush(pq,x)