"""
id: 1916
title:최소비용구하기
ac:https://www.acmicpc.net/source/45134398
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
5
4
1 2 1
3 1 10
3 1 100
2 3 2
2 3
""".strip())

import sys,collections,heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = collections.defaultdict(list)
for _ in range(M):
    v,w,cost = map(int,input().split())
    graph[v].append((cost,w))

src,dest = map(int,input().split())
# print(graph, src, dest)

pqueue = [(0,src)] # cost,start
distance = collections.defaultdict()
while pqueue:
    cost,node = heapq.heappop(pqueue)
    if node not in distance:
        distance[node] = cost
        for _cost,v in graph[node]:
            heapq.heappush(pqueue,(cost+_cost,v))

# print(distance)
print(distance[dest])
