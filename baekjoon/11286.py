"""
id: 11296
title:절댓값힙
ac:https://www.acmicpc.net/source/44746971
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
""".strip())

import sys
from heapq import *
N = int(sys.stdin.readline().strip())
h = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        try:
            print(heappop(h)[1])
            # abs_y, y = heappop(h)
            # print(y)
        except Exception:
            print(0)
    else:
        heappush(h,(abs(x),x))