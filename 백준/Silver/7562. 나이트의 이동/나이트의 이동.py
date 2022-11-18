import collections

dxy = [(-2,1),(-2,-1),(-1,2),(-1,-2),
        (1,2),(1,-2),(2,1),(2,-1)]
l = 0
def bfs(src,dest):
    q = collections.deque([(*src,0)])
    vis = set()
    while q:
        x,y,cnt = q.popleft()
        if (x,y) == dest:
            return cnt
        if (x,y) in vis:
            continue
        vis.add((x,y))
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not(0<=nx<l and 0<=ny<l):
                continue
            q.append((nx,ny,cnt+1))
    return -1

for _ in range(int(input())):
    l = int(input())
    cur = tuple(map(int,input().split()))
    nex = tuple(map(int,input().split()))
    cnt = bfs(cur,nex)
    print(cnt)