import sys, collections, heapq, math, re, random
input=sys.stdin.readline

N=int(input())
r1,c1,r2,c2 = map(int,input().split())

q = collections.deque([(r1,c1,0)])
vis = set()
dxy = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]
while q:
    x,y,cnt = q.popleft()
    if (x,y) in vis: continue
    vis.add((x,y))
    if (x,y)==(r2,c2):
        print(cnt)
        exit()
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if not (0<=nx<N and 0<=ny<N):
            continue
        q.append((nx,ny,cnt+1))
print(-1)