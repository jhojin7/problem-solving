import collections
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

def holes(xx,yy):
    if grid[xx][yy]==1: return set()
    q=collections.deque([(xx,yy)])
    dxy = [(-1,0),(0,-1),(1,0),(0,1)]
    vis = set()
    while q:
        x,y=q.popleft()
        if (x,y) in vis: continue
        vis.add((x,y))
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if grid[nx][ny]==1: 
                continue
            if nx==0 or nx==N-1 or ny==0 or ny==M-1:
                return set()
            q.append((nx,ny))
    return vis

def check(x,y):
    dxy = [(-1,0),(0,-1),(1,0),(0,1)]
    if grid[x][y]==0: return False
    cnt=0
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not (0<=nx<N and 0<=ny<M):
            continue
        if len(holes(nx,ny))!=0:
            continue
        if grid[nx][ny]==0:
            cnt+=1
    if cnt>=2: return True
    return False

t=0
while 1:
    cnt=0
    for row in grid:
        cnt+=row.count(1)
    if cnt==0: break
    erase=[]
    for i in range(N):
        for j in range(M):
            if check(i,j):
                erase.append((i,j))
    for i,j in erase:
        grid[i][j]=0
    t+=1
print(t)