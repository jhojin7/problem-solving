import collections
def solution(maps):
    N,M = len(maps),len(maps[0])
    dxy = [(-1,0),(0,-1),(1,0),(0,1)]
    q = collections.deque([(0,0,1)])
    vis = set()
    while q:
        x,y,cnt = q.popleft()
        if (x,y)==(N-1,M-1): 
            return cnt
        if (x,y) in vis: continue
        vis.add((x,y))
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not (0<=nx<N and 0<=ny<M): continue
            if maps[nx][ny]==0: continue
            q.append((nx,ny,cnt+1))
    return -1