from copy import deepcopy
N,M,T = map(int,input().split())
K,a,b = map(int,input().split())
grid = []
for _ in range(N):
    row = list(input().strip())
    grid.append(row)

def check(xx,yy):
    life = 0
    for i in range(xx-K,xx+K+1):
        for j in range(yy-K,yy+K+1):
            if i==xx and j==yy:
                continue
            if not (0<=i<N and 0<=j<M):
                continue
            if grid[i][j]=='*':
                life+=1
    return life

for _ in range(T):
    nxt = deepcopy(grid)
    for i in range(N):
        for j in range(M):
            chk = check(i,j)
            if grid[i][j]=='*' and a<=chk<=b:
                nxt[i][j] = '*'
            elif grid[i][j]=='*' and chk<a:
                nxt[i][j] = '.'
            elif grid[i][j]=='*' and b<chk:
                nxt[i][j] = '.'
            elif grid[i][j]=='.' and a<chk<=b:
                nxt[i][j] = '*'
    grid = deepcopy(nxt)

for row in nxt:
    print(''.join(row))