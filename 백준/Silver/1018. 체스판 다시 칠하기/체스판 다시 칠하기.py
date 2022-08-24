import collections
N,M = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(input().strip()))

bw = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]
wb = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

def check(xx,yy):
    bwbw,wbwb=0,0
    for i in range(8):
        for j in range(8):
            if grid[xx+i][yy+j]!=bw[i][j]: bwbw+=1
            if grid[xx+i][yy+j]!=wb[i][j]: wbwb+=1
    return min(bwbw,wbwb)

mincnt = 99999
for i in range(N-7):
    for j in range(M-7):
        mincnt = min(check(i,j),mincnt)
print(mincnt)