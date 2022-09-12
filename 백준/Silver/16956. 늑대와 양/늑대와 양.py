r,c=map(int,input().split())
grid = []
for _ in range(r):
    row = list(input().strip())
    for j in range(len(row)):
        if row[j]=='.': row[j]='D'
    grid.append(row)

dxy = [(-1,0),(1,0),(0,1),(0,-1)]
for i in range(r):
    for j in range(c):
        for dx,dy in dxy:
            nx,ny=i+dx,j+dy
            if not (0<=nx<r
                and 0<=ny<c): continue
            elif (grid[i][j]=='S'
                and grid[nx][ny]=='W'):
                # print(nx,ny,grid[nx][ny])
                print(0)
                exit()
print(1)
for r in grid:
    print(*r,sep='')