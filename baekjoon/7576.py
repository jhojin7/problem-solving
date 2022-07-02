"""
id: 7576
title:토마토
ac:https://www.acmicpc.net/source/45394214
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2 2
1 -1
-1 1
""".strip())

import sys, collections
input = sys.stdin.readline

def bfs():
    days = 0
    queue = collections.deque(tomatoes)
    adjacent = [(0,1),(1,0),(0,-1),(-1,0)]
    while queue:
        I,J,days = queue.popleft()
        for i,j in adjacent:
            new_i,new_j = I+i,J+j
            if (0<=new_i<N and 0<=new_j<M
                and grid[new_i][new_j] == 0): 
                grid[new_i][new_j] = 1
                queue.append((new_i,new_j,days+1))
        # print(days,I,J,queue)
        # print(*grid,sep='\n')

    for row in grid:
        if 0 in row:
            return (-1)
    return days

M,N = map(int,input().split())
grid = []
tomatoes = []
for i in range(N):
    row = list(map(int,input().split()))
    grid.append(row)
    for j in range(len(row)):
        if grid[i][j] == 1: 
            tomatoes.append((i,j,0)) 
# print(M,N,grid, tomatoes)
print(bfs())