import sys,collections, heapq,math, re
# input = sys.stdin.readline

N=int(input())
M = 6*(N//3)
arr=[[' ' for _ in range(M)] for _ in range(N)]
def solve(x,y,z):
    # print(x,y,z)
    arr[x][y] = '*'
    if z==3: 
        arr[x+1][y-1] = '*'
        arr[x+1][y+1] = '*'
        # arr[x+2][y-2] = '*'
        for j in range(y-2,y+2+1):
            arr[x+2][j] = '*'
        return
    solve(x+z//2,y-z//2,z//2)
    solve(x+z//2,y+z//2,z//2)
    solve(x,y,z//2)

solve(0,M//2,N)
for row in arr:
    print(*row[1:],sep='')