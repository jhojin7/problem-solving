import collections

N,M = map(int,input().split())
grid = []
J = F = None
Fs = []
for i in range(N):
    row =input().strip()
    grid.append(list(row))
    for j in range(M):
        if not J and grid[i][j]=='J': J = (i,j)
        if grid[i][j]=='F':
            F = (i,j)
            Fs.append((*F,0))# i,j,dist
dxy = [(0,1),(1,0),(-1,0),(0,-1)]

# bfs fire
visited = set()
queue = collections.deque(Fs)
while queue:
    x,y,dist = queue.popleft()
    # visit
    if (x,y) in visited: continue
    if (grid[x][y] not in "#JF"
        and grid[x][y]<str(dist)):
        grid[x][y] = dist
    visited.add((x,y))
    # append queue
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not(0<=nx<N and 0<=ny<M):
            continue
        if ((nx,ny) not in visited
            and grid[nx][ny]=='.'):
            queue.append((nx,ny,dist+1))

# bfs jihun
safe = False
ansdist = None
visited = set()
queue = collections.deque([(*J,0)])
while queue:
    x,y,dist = queue.popleft()
    # visit
    if safe: break
    if (x,y) in visited: continue
    if (str(grid[x][y]) not in "#JF"):
        grid[x][y] = 'J' # mark J
    visited.add((x,y))

    # append queue
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        # if jihun can escape grid, dist+1
        if not (0<=nx<N and 0<=ny<M):
            ansdist = dist+1
            safe = True
            break
        if (nx,ny) not in visited:
            if (type(grid[nx][ny])==type(1)
                and grid[nx][ny]>dist+1):
                queue.append((nx,ny,dist+1))
            elif (str(grid[nx][ny]) not in "#JF"
                and grid[nx][ny]=='.'):
                queue.append((nx,ny,dist+1))
if not safe: print("IMPOSSIBLE")
else: print(ansdist)