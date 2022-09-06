import collections

grid =[]
for i in range(12):
    grid.append(list(input().strip()))

# dxy = [(0,1),(-1,0),(0,-1),(1,0)]
dxy = [(-1,0),(0,1),(1,0),(0,-1)]
def bfs(i,j):
    q = collections.deque([(i,j)])
    vis=set()
    while q:
        x,y = q.popleft()
        # if (x,y) in vis: break
        # vis.add((x,y))
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not (0<=nx<12 and 0<=ny<6):
                continue
            if (grid[nx][ny]==grid[i][j]
                and (nx,ny) not in vis):
                q.append((nx,ny))
                vis.add((nx,ny))
    return vis

def fall(x,y):
    cur = grid[x][y]
    grid[x][y] = '.'
    ii = x
    for i in range(x+1,len(grid)):
        if grid[i][y] in "RGBPY":
            continue
        else:
            ii = i
    grid[ii][y] = cur

popped = 0
while 1:
    cnt = 0
    # pop
    # for i in range(12):
    #     for j in range(6):
    for i in range(11,-1,-1):
        for j in range(5,-1,-1):
            if grid[i][j]!='.':
                ret = bfs(i,j)
                if len(ret)<4: continue
                cnt+=1
                for x,y in sorted(ret):
                    grid[x][y]='.'
    # fall
    for i in range(11,-1,-1):
        for j in range(5,-1,-1):
            if grid[i][j]!='.': 
                fall(i,j)
    # if no more to pop, break
    if cnt==0: break
    popped+=1
#     print(*grid,cnt)
#     print()
# # print(*grid)
print(popped)