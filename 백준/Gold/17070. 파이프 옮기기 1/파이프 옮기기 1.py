import collections
N=int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

def check(xx,yy,zz):
    if zz==0 or zz==1:
        if grid[xx][yy]!=0: 
            return False
    elif zz==2:
        if (grid[xx][yy]!=0
            or grid[xx-1][yy]!=0
            or grid[xx][yy-1]!=0):
            return False
    return True

q = [(0,1,0)]
dxyz = [
    [(0,1,0),(1,1,2)],
    [(1,0,1),(1,1,2)],
    [(0,1,0),(1,0,1),(1,1,2)],
] # z = 0- 1| 2\
cnt=0
while q:
    x,y,z = q.pop()
    # print(x,y,z)
    if (x,y)==(N-1,N-1):
        cnt+=1
        continue
    for dx,dy,dz in dxyz[z]:
        nx,ny,nz = x+dx,y+dy,dz
        if not (0<=nx<N and 0<=ny<N):
            continue
        # check walls
        if not check(nx,ny,nz):
            continue
        q.append((nx,ny,nz))
print(cnt)
