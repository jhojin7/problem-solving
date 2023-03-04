import sys, collections, itertools, heapq, math, re, random
from copy import deepcopy
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
ggrid = [list(inputint()) for _ in range(N)]
# 1up 2down 3left 4right

def do_row(row:list,dir):
    if dir in [2,4]:
        row.reverse()
        # row = list(reversed(row))
    # row = [16,0,2,2]
    n=len(row)
    # print(dir,row)
    for i in range(n):
        if row[i]==0:
            for _ in range(20):
                if row[i]==0: row.append(row.pop(i))
                else:break
            # continue
    for i in range(n-1):
        if row[i]==0: break
        if row[i]==row[i+1]:
            row[i]*=2
            row.pop(i+1)
            row.append(0)
    if dir in [2,4]:
        row.reverse()
    return row

def execute(_grid,dir):
    grid = _grid.copy()
    # print(grid)
    if dir in [3,4]:
        rows = [row for row in grid]
        for i in range(N):
            rows[i] = do_row(rows[i],dir)
        return rows
    elif dir in [1,2]:
        cols = [[grid[i][j] for i in range(N)] for j in range(N)]
        for i in range(N):
            cols[i] = do_row(cols[i],dir)
        return [[cols[i][j] for i in range(N)] for j in range(N)]

def dfs(grid,cnt):
    if cnt==0:
        return max([max(row) for row in grid])
    ans = 0
    for dir in [1,2,3,4]:
        # grid = execute(grid,dir)
        ans = max(ans,dfs(
            execute(deepcopy(grid),dir),cnt-1))
        # grid = rollback(grid,dir)
    return ans
print(dfs(deepcopy(ggrid),5))