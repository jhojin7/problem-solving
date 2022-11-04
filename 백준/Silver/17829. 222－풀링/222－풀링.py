import sys
sys.setrecursionlimit(2**10)

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

def backtrack(x0,y0,x1,y1):
    # print(x0,y0,x1,y1)
    xm,ym = (x0+x1)//2,(y0+y1)//2
    if x0==xm and y0==ym:
        return sorted([
            grid[x0][y0],grid[x0][ym],
            grid[xm][y0],grid[xm][ym],
        ])[2]
    a=backtrack(x0,y0,xm,ym)
    b=backtrack(x0,ym,xm,y1)
    c=backtrack(xm,y0,x1,ym)
    d=backtrack(xm,ym,x1,y1)

    # print(a,b,c,d)
    return sorted([a,b,c,d])[2]

ans = backtrack(0,0,N,N)
print(ans)