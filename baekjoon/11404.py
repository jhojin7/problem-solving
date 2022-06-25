"""
id: 11404
title:플로이드
ac:https://www.acmicpc.net/source/45004312
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2
1
1 2 100
""".strip())

import sys, math
N = int(input())
M = int(input())
edges = [[math.inf for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    src,dest,cost = map(int,sys.stdin.readline().split())
    edges[src][dest] = min(cost, edges[src][dest])

for i in range(1,N+1):
    edges[i][i] = 0

# floyd-warshall
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j: edges[i][j] = 0
            if edges[i][j] > edges[i][k] + edges[k][j]:
                edges[i][j] = edges[i][k] + edges[k][j]

for i in range(1,N+1):
    for j in range(1,N+1):
        if edges[i][j] == math.inf:
            print("0",end=' ')
        else:
            print(edges[i][j],end=' ')
    print()

    # print(*edges[i][1:],sep=' ')