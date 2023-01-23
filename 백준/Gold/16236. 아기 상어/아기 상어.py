import collections
N=int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

bx,by=0,0
fish=[]
eaten=0
size=2

for i in range(N):
    for j in range(N):
        if grid[i][j]==9: bx,by=i,j
        if 0<grid[i][j]<9: fish.append((i,j))

dxy=[(-1,0),(0,-1),(1,0),(0,1)]
def dist(src,dest):
    q=collections.deque([(src[0],src[1],0)])
    vis=set()
    ans=99999
    while q:
        x,y,d = q.popleft()
        if (x,y)==dest:
            ans=min(ans,d)
        if (x,y) in vis: continue
        vis.add((x,y))
        for dx,dy in dxy:
            nx,ny=x+dx,y+dy
            if not (0<=nx<N and 0<=ny<N):
                continue
            if grid[nx][ny]>size:
                continue
            # if (nx,ny) in vis: 
            #     continue
            q.append((nx,ny,d+1))
    return ans

def nearest(xx,yy):
    mindist = 99999
    ret = -99999
    for i,xy in enumerate(fish):
        nx,ny=xy
        if grid[nx][ny]>=size: continue
        d = dist((xx,yy),(nx,ny))
        if d==99999: continue
        if d<mindist:
            mindist=d
            ret=i
    if ret==-99999: return (-999,-999)
    return fish.pop(ret)

# print(dist((2,2),(0,0)))
# # print(nearest(2,2))
t=0
grid[bx][by]=0
while fish:
    # fish.sort()
    # # fish.reverse()
    nx,ny = nearest(bx,by)
    if (nx,ny)==(-999,-999): break
    if grid[nx][ny]<size: eaten+=1
    dd = dist((bx,by),(nx,ny))
    if eaten==size: 
        size+=1
        eaten=0
    # print((bx,by),dd)
    t+=dd
    grid[bx][by]=0
    bx,by = nx,ny
print(t)