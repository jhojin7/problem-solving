grid = [list(map(int,input().strip())) for _ in range(9)]

def backtrack(k):
    if k==len(empty):
        for g in grid: print(*g,sep='')
        exit()
    x,y = empty[k]
    for n in range(1,10):
        ok1,ok2,ok3 = True,True,True
        for i in range(9):
            # horizontal
            if grid[x][i]==n: #grid[x][y]:
                # print(x,i)
                ok1=False
                break
            # vertical
            if grid[i][y]==n: #grid[x][y]:
                # print(i,y)
                ok2=False
                break
        
        xa = x//3*3
        ya = y//3*3
        for i in range(xa,xa+3):
            for j in range(ya,ya+3):
                if grid[i][j]==n: #grid[x][y]:
                    ok3 = False
                    break

        grid[x][y] = n ##################
        if ok1 and ok2 and ok3: 
            backtrack(k+1)
        grid[x][y] = 0

empty = []
for i in range(9):
    for j in range(9):
        if grid[i][j]==0:
            empty.append((i,j))

backtrack(0)