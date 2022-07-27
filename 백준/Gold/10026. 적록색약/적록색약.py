import sys,collections
from copy import deepcopy
input = sys.stdin.readline
N = int(input())
grid = []
grid_colorblind = []
for i in range(N):
    row = list(input().strip())
    grid.append(row)
#RG
grid_colorblind = deepcopy(grid)
for i in range(N):
    for j in range(N):
        if grid_colorblind[i][j]=='G': 
            grid_colorblind[i][j]='R'
# print(grid)
# print(grid_colorblind)

def bfs(grid,i,j):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = collections.deque([(i,j)])
    rgb = grid[i][j]
    cnt = 0
    while queue:
        x,y = queue.popleft()
        if grid[x][y] != rgb:
            continue
        else:
            grid[x][y] = '0'
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if not (0<=nx<N and 0<=ny<N): continue
            if grid[nx][ny] == '0': continue
            # if rgb=='R' and grid[nx][ny] == 'G':
            #     grid[nx][ny] = 'g'
            if grid[nx][ny] == rgb:
                queue.append((nx,ny))
    return cnt

def do_bfs(grid):
    cnt = 0
    rgbs = []
    for i in range(N):
        for j in range(N):
            if grid[i][j]!='0':
                # print(grid[i][j])
                rgbs.append(grid[i][j])
                bfs(grid,i,j)
                # print(grid)
    # print(rgbs)
    return len(rgbs)

print(do_bfs(grid),do_bfs(grid_colorblind))