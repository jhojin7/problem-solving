import sys,collections
input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

def bfs(i,j):
    size = 0
    queue = collections.deque([(i,j)])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    while queue:
        ci,cj = queue.popleft()
        size += 1
        arr[ci][cj] = 0
        for di,dj in directions:
            next_i,next_j = ci+di,cj+dj
            if not (0<=next_i<n and 0<=next_j<m): continue
            if arr[next_i][next_j] == 1:
                arr[next_i][next_j] = 0
                queue.append((next_i,next_j))
    return size

cnt = 0
maxsize = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            size = bfs(i,j)
            maxsize = max(maxsize,size)
            cnt+=1
print(cnt)
print(maxsize)