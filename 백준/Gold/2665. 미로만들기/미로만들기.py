import collections, math, heapq

N = int(input())
grid = []
for _ in range(N):
    row = list(map(int,input().strip()))
    grid.append(row)
# print(grid)

mink = math.inf
flag = 0

vis = [[False for _ in range(N)] for _ in range(N)]
# vis[0][0]=0
q = [(0,0,0)]
dxy=[(-1,0),(0,-1),(1,0),(0,1)]
# vis = collections.defaultdict(int)

while q:
    # print(q)
    # x,y,k = q.popleft()
    k,x,y = heapq.heappop(q)
    if (x,y)==(N-1,N-1):
        # print(x,y,k)
        # mink = min(mink,k)
        print(k)
        break
    if vis[x][y]:
        continue
    vis[x][y]=True

    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not (0<=nx<N and 0<=ny<N):
            continue
        if vis[nx][ny]:
            continue
        if grid[nx][ny]==1:
            heapq.heappush(q,(k,nx,ny))
            # q.append((nx,ny,k))
        if grid[nx][ny]==0:
            heapq.heappush(q,(k+1,nx,ny))
            # q.append((nx,ny,k+1))