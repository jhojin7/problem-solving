N,M=map(int,input().split())
grid = []
for _ in range(N):
    row = list(input().strip())
    grid.append(row)

dxy = [(0,1),(1,0),(0,-1),(-1,0)]
stack = [(0,0,0,str(grid[0][0]))]
maxdist = -9999999
while stack:
    x,y,dist,vis = stack.pop()
    maxdist = max(len(vis),maxdist)
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if ((0<=nx<N and 0<=ny<M)
            and grid[nx][ny] not in vis):
            stack.append((nx,ny,dist+1,vis+grid[nx][ny]))
print(maxdist)