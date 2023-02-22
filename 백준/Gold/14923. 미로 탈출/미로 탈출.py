import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N,M = inputint()
Hx,Hy = inputint()
Ex,Ey = inputint()
Hx,Hy,Ex,Ey=Hx-1,Hy-1,Ex-1,Ey-1
grid = [list(inputint()) for _ in range(N)]

dxy = [(-1,0),(0,-1),(1,0),(0,1)]
q = collections.deque([(Hx,Hy,0,0)])
vis = set()
ok=False
while q:
    x,y,dist,used = q.popleft()
    # print(x,y,dist,used)
    if (x,y)==(Ex,Ey): 
        # print("aaaaa")
        # print(x,y,dist,used)
        print(dist)
        ok=True
        break
        # exit()
    if (x,y,used) in vis: continue
    vis.add((x,y,used))
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not (0<=nx<N and 0<=ny<M): continue
        if grid[nx][ny]==1:
            if used==0: q.append((nx,ny,dist+1,1))
        else:
            q.append((nx,ny,dist+1,used))
if not ok: print(-1)