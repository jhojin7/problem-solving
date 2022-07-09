import sys
input = sys.stdin.readline
N, M = map(int,input().split())   

arr = [[0 for _ in range(M+1)]]
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append([0]+row)

K = int(input())
# 2057
for _ in range(K):
    i,j,x,y = map(int,input().split())
    s = 0
    for a in range(i,x+1):
        for b in range(j,y+1):
            s += arr[a][b]
    print(s)