import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

grid = []
for _ in range(9):
    grid.append(list(input().split()))
# print(grid)

def g(x,y): return grid[x][y]
arr = [
    (1,1,1),
    (2,1,4),
    (3,1,7),
    (4,4,7),
    (5,7,7),
    (6,7,4),
    (7,7,1),
    (8,4,1),
]
mid = [(x,y,g(x,y)) for z,x,y in arr]
mid.sort(key=lambda m:m[2])
# print(mid)

for i,mm in enumerate(mid,1):
    x,y,m = mm
    print(f"#{i}. {m}")
    tasks = [g(x-1,y-1),g(x-1,y),g(x-1,y+1),
        g(x,y+1),g(x+1,y+1),g(x+1,y),
        g(x+1,y-1),g(x,y-1),]
    tasks.sort()
    for j,t in enumerate(tasks,1):
        print(f"#{i}-{j}. {t}")