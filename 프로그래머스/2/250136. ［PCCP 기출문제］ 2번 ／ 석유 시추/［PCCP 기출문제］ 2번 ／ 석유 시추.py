import collections
def solution(land):
    N = len(land)
    M = len(land[0])
    VIS = [[0 for _ in range(M)] for _ in range(N)]
    CNT = [0 for _ in range(M)]
    
    
    def bfs(i,j):
        q = collections.deque()
        q.append((i,j))
        vis = set()
        cnt=0
        while q:
            x,y = q.popleft()
            if (x,y) in vis:
                continue
            vis.add((x,y))
            VIS[x][y] = 1
            cnt+=1
            dxy = [(-1,0),(1,0),(0,-1),(0,1)]
            for dx,dy in dxy:
                nx, ny = x+dx, y+dy
                if not (0<=nx<N and 0<=ny<M):
                    continue
                if land[nx][ny] == 0:
                    continue
                q.append((nx,ny))
        yy = set([y for x,y in vis])
        for y in yy:
            CNT[y] += cnt
        return cnt
                
    oils = collections.defaultdict(list)
    for j in range(M):
        for i in range(N):
            if land[i][j]==0 or VIS[i][j]==1:
                continue
            cnt = bfs(i,j)
    return (max(CNT))
            
