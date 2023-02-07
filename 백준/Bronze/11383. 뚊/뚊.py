import sys, collections, heapq, math, re
input=sys.stdin.readline
N,M = map(int,input().split())
grid1 = [list(input().strip()) for _ in range(N)]
grid2 = [list(input().strip()) for _ in range(N)]
grid3 = []
for row in grid1:
    tmp=[]
    for x in row:
        tmp.append(x)
        tmp.append(x)
    grid3.append(tmp)

if grid2==grid3:
    print("Eyfa")
else: 
    print("Not Eyfa")