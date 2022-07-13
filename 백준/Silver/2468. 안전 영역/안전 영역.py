import sys,collections,copy
input = sys.stdin.readline

N = int(input())
arr = []
max_h = 0
for _ in range(N):
    row = list(map(int,input().split()))
    max_h = max(max_h,max(row))
    arr.append(row)

def bfs(_arr,i,j):
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    queue = collections.deque([(i,j)])
    while queue:
        ii,jj = queue.popleft()
        if _arr[ii][jj] == -1:
            continue
        _arr[ii][jj] = -1
        for di,dj in directions:
            nexti,nextj = ii+di,jj+dj
            if not(0<=nexti<N and 0<=nextj<N): continue
            if _arr[nexti][nextj] == -1: continue
            queue.append((nexti,nextj))

max_safe = 0
for h in range(max_h+1):
    arr2 = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if arr2[i][j] <= h:
                arr2[i][j] = -1
    safe = 0
    for i in range(N):
        for j in range(N):
            if arr2[i][j] != -1:
                bfs(arr2,i,j)
                safe+=1
    max_safe = max(max_safe,safe)
print(max_safe)