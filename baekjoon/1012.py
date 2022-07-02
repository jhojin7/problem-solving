"""
id: 1012
title:유기농배추
ac:https://www.acmicpc.net/source/45408576
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2
50 50 3
48 48
49 49
48 49
1 1 1
0 0
""".strip())

adjacent = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(I,J):
    visited = []
    queue = collections.deque([(I,J)])

    if grid[I][J] == 1:
        visited.append((I,J))

    while queue:
        _i,_j = queue.pop()
        for a,b in adjacent:
            new_i,new_j = _i+a,_j+b
            if (0<=new_i<N and 0<=new_j<M
                and grid[new_i][new_j] == 1):
                grid[new_i][new_j] = 0
                visited.append((_i,_j))
                queue.append((new_i,new_j))
    return visited

import sys,collections
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    grid = [[0 for _ in range(M)] for _ in range(N)]
    sols = []
    for _ in range(K):
        y,x = map(int,input().split())
        # print((x,y))
        grid[x][y] = 1

    # print(*grid,sep='\n')
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                sol = bfs(i,j)
                if sol != []:
                    sols.append(sol)

    # print(sols,len(sols))
    print(len(sols))