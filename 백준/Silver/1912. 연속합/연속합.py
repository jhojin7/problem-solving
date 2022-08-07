import math, sys
input = sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))

# kadane
curmax, globalmax = 0, -math.inf
for i in range(N):
    curmax += arr[i]
    if globalmax < curmax: 
        globalmax = curmax
    if curmax < 0:
        curmax = 0
print(globalmax)