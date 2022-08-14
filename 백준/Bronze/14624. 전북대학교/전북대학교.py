N=int(input())
if N%2==0: print("I LOVE CBNU")
else:
    grid = [['' for _ in range(N)] for _ in range(N)]
    for j in range(N):
        grid[0][j] = '*'
    j = N//2
    jj = N//2
    for i in range(1,N):
        if j<0 or jj>N: break
        grid[i][j] = '*'; j-=1
        grid[i][jj] = '*'; jj+=1
        for k in range(jj):
            if grid[i][k]!='*':
                grid[i][k] = ' '

    for i in range(len(grid)):
        for c in grid[i]:
            print(c,end='')
        if i+1!=len(grid): print('')