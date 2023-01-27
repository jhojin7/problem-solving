import sys,collections, heapq,math
input = sys.stdin.readline

R,C,T=map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(R)]

def spread(_tmp,x,y):
    nxt = grid[x][y]//5
    cnt = 0
    dxy = [(-1,0),(0,-1),(1,0),(0,1)]
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not (0<=nx<R and 0<=ny<C):
            continue
        if grid[nx][ny]==-1: 
            continue
        cnt+=1
        # grid[nx][ny] = nxt
        _tmp[nx][ny]+=nxt
    # grid[x][y] = grid[x][y]-nxt*cnt
    _tmp[x][y] += grid[x][y]-nxt*cnt

def rotate(xa,ya,xb,yb,clockwise=True):
    data = collections.deque()
    for i in range(xa,xb):
        data.append(grid[i][ya])
    for j in range(ya,yb):
        data.append(grid[xb][j])
    for i in range(xb,xa,-1):
        data.append(grid[i][yb])
    for j in range(yb,ya,-1):
        data.append(grid[xa][j])
    # print(data)
    if clockwise:
        data.popleft() # pop-1
        data.append(data.popleft()) #
        data.appendleft(-1)
        # print(data)
    else:
        data.appendleft(data.pop()) #
        # # do -1 later
        # print(data)

    idx = 0
    for i in range(xa,xb):
        grid[i][ya] = data[idx]; idx+=1 
    for j in range(ya,yb):
        grid[xb][j] = data[idx]; idx+=1 
    for i in range(xb,xa,-1):
        grid[i][yb] = data[idx]; idx+=1 
    for j in range(yb,ya,-1):
        grid[xa][j] = data[idx]; idx+=1 

    if not clockwise:
        grid[xb][ya],grid[xb][ya+1] = \
            grid[xb][ya+1],grid[xb][ya]
    
    # purify air
    if clockwise: grid[xa][1]=0
    else: grid[xb][1] = 0

for _ in range(T):
    # 1
    tmp = [[0 for _ in range(C)] for _ in range(R)]
    purifier = (0,0)
    for i in range(R):
        for j in range(C):
            if grid[i][j]>0: 
                spread(tmp,i,j)
            elif grid[i][j]==-1:
                purifier = (i,j)
                tmp[i][j] = -1
    for i in range(R):
        for j in range(C):
            grid[i][j] = tmp[i][j]
    # print(*grid,sep='\n')
    # print()

    xa,ya = 0,0
    xb,yb = purifier[0]-1,C-1
    rotate(xa,ya,xb,yb,False)
    xa,ya = purifier[0],purifier[1]
    xb,yb = R-1,C-1
    rotate(xa,ya,xb,yb,True)
    # print(*grid,sep='\n')

# print(*grid,sep='\n')
ans = sum([sum(row) for row in grid])+2
print(ans)