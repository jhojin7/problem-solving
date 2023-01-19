import collections

N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
empty = []
for i in range(N):
    for j in range(M):
        if grid[i][j]==0:
            empty.append((i,j))

dxy = [(-1,0),(0,-1),(1,0),(0,1)]
def spread(_grid,xx,yy):
    q=collections.deque([(xx,yy)])
    vis = set()
    while q:
        x,y = q.popleft()
        if (x,y) in vis: continue
        vis.add((x,y))
        _grid[x][y] = 2
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not (0<=nx<N and 0<=ny<M):
                continue
            if _grid[nx][ny]==1: continue
            if _grid[nx][ny]==2: continue
            q.append((nx,ny))

def check(_grid):
    for i in range(N):
        for j in range(M):
            if _grid[i][j]==2:
                spread(_grid,i,j)

import copy, itertools
combs = itertools.combinations(empty,3)
ans =0

for comb in combs:
    _grid = copy.deepcopy(grid)
    for i,j in comb:
        _grid[i][j]=1
    check(_grid)
    tmp =0
    for row in _grid:
        tmp+=row.count(0)
    ans = max(ans,tmp)
print(ans)

# def backtrack(idx,wall):
#     if wall==3:
#         print()
#         return
#     for i in range(len(empty)):
#         if i==idx: continue
#         print(i,end=' ')
#         backtrack(i,wall+1)
# backtrack(0,0)