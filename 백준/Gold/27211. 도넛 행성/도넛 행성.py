import collections

N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
dxy = [(-1,0),(0,-1),(1,0),(0,1)]

def bfs(xx,yy):
    q = collections.deque([(xx,yy)])
    vis = set()
    while q:
        x,y = q.popleft()
        if (x,y) in vis: continue
        vis.add((x,y))
        grid[x][y] = 1
        for dx,dy in dxy:
            nx,ny = (N+x+dx)%N,(M+y+dy)%M
            if grid[nx][ny]==1: continue
            q.append((nx,ny))

ans=0
for i in range(N):
    for j in range(M):
        if grid[i][j]==0:
            bfs(i,j)
            ans+=1
            # print(grid)
print(ans)