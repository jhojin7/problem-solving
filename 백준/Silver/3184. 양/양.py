import collections

R,C = map(int,input().split())
grid = []
for _ in range(R):
    row = list(input().strip())
    grid.append(row)

def bfs(i,j):
    o,v= 0,0
    queue = collections.deque([(i,j)])
    visited = set()
    dxy = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        x,y = queue.popleft()
        if (x,y) in visited: continue
        if grid[x][y]=='#': continue
        visited.add((x,y))
        if grid[x][y]=='o': o+=1
        if grid[x][y]=='v': v+=1

        grid[x][y] = '%'
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if (0<=nx<R and 0<=ny<C
                and grid[nx][ny]!='#'):
                queue.append((nx,ny))
    return o,v

ooo,vvv = 0,0
for i in range(R):
    for j in range(C):
        if (grid[i][j]!='#'
            and grid[i][j]!='%'):
            o,v = bfs(i,j)
            # print(o,v)
            if o>v: ooo+=o 
            else: vvv+=v
print(ooo,vvv)