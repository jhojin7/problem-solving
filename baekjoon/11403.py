"""
id: 11403
title:경로찾기
ac:https://www.acmicpc.net/source/45242740
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
3
0 1 0
0 0 1
1 0 0
""".strip())

import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    row = list(map(int,input().split()))
    graph.append(row)
# print(graph)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] + graph[k][j] > 1:
                graph[i][j] = 1

for i in range(N):
    print(*graph[i])