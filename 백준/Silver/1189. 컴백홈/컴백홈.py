import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N,M,K = inputint()
grid = [list(inputchars()) for _ in range(N)]
cnt =0
vis =set()
dxy = [(-1,0),(0,-1),(1,0),(0,1)]

def dfs(x,y,k):
    global cnt
    if (x,y)==(0,M-1) and k==K:
        cnt+=1
        return
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not (0<=nx<N and 0<=ny<M):
            continue
        if grid[nx][ny]=='T':
            continue
        if (nx,ny) in vis: 
            continue
        vis.add((nx,ny))
        dfs(nx,ny,k+1)
        vis.remove((nx,ny))
vis.add((N-1,0))
dfs(N-1,0,1)
print(cnt)