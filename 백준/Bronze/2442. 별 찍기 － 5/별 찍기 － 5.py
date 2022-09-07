N=int(input())
grid = [['' for _ in range(2*N+1)] for _ in range(N)]
m=(2*N+1)//2
for i in range(N):
    for j in range(m-i-1,m+i):
        grid[i][j]='*'
for i in range(N):
    for j in range(m+i):
        if grid[i][j]=='*': print("*",end='')
        else: print(" ",end='')
    print()