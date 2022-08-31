from itertools import combinations, permutations

N,M=map(int,input().split())
grid = []
house,chicken=[],[]
for i in range(N):
    grid.append(list(map(int,input().split())))
    for j in range(N):
        if grid[i][j]==1: house.append((i,j))
        if grid[i][j]==2: chicken.append((i,j))
dist = []
for r in range(1,M+1):
    for combi in combinations(chicken,r):
        tmp =[]
        for i,j in house:
            d = 9999999
            for chi in combi:
                x,y=chi
                d=min(d,abs(x-i)+abs(y-j))
            tmp.append(d)
        dist.append(sum(tmp))
print(min(dist))