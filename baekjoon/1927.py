"""
id: 1927
title:최소힙
ac:https://www.acmicpc.net/source/44700041 
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
9
0
12345678
1
2
0
0
0
0
32
""".strip())

import sys, heapq
input = sys.stdin.readline
N = int(input())
minheap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        try: print(heapq.heappop(minheap))
        except IndexError: print(0)
    else:
        heapq.heappush(minheap, x)