import collections

M,N,H = map(int,input().split())
box = []
for i in range(H):
    floor = [list(map(int,input().split())) for _ in range(N)]
    box.append(floor)

# down, r,l,fr,re, up
dx = [-1,0,0,0,0,1]
dy = [0,-1,0,1,0,0]
dz = [0,0,-1,0,1,0]

def bfs(xx,yy,zz):
    q = collections.deque([(xx,yy,zz)])
    while q:
        x,y,z = q.popleft()
        for i in range(6):
            nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
            if not (0<=nx<H and 0<=ny<N and 0<=nz<M): continue
            # if box[nx][ny][nz]!=0: continue
            if box[nx][ny][nz]==-1: continue
            if 1<= box[nx][ny][nz] <= box[x][y][z]+1:
                continue
            box[nx][ny][nz] = box[x][y][z]+1
            q.append((nx,ny,nz))

for x in range(H):
    for y in range(N):
        for z in range(M):
            if box[x][y][z]==1:
                bfs(x,y,z)
ans = 0
for floor in box:
    for row in floor:
        if 0 in row:
            print(-1)
            exit()
        else:
            ans=max(ans,max(row))

# print(*box,sep='\n')
print(ans-1)