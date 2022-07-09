import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def sol():
    W,H = map(int,input().split())
    if (W,H) == (0,0): return -1
    arr = []
    cnt = 0
    for _ in range(H):
        row = map(int,input().split())
        arr.append(list(row))

    def dfs(i,j,cnt):
        if arr[i][j] == -1 or arr[i][j] == 0:
            return cnt
        arr[i][j] = -1
        
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1),
                        (1,1),(-1,1),(1,-1),(-1,-1)]:
            next_i,next_j = i+di,j+dj
            if ((0<=next_i<H and 0<=next_j<W)
                and arr[next_i][next_j] == 1):
                dfs(next_i,next_j,cnt+1)

    for i in range(H):
        for j in range(W):
            if arr[i][j] ==1:
                dfs(i,j,0)
                cnt+=1
    print(cnt)

while True:
    if sol() == -1:
        break