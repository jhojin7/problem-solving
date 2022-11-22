grid = []
for i in range(5):
    row = list(map(int,input().split()))
    grid.append(row)

def remove(call):
    for i in range(5):
        for j in range(5):
            if grid[i][j]==call:
                grid[i][j] = -1
                return
                # return (i,j,call)

def check():
    bingo=0
    # diag
    cnt1,cnt2 = 0,0
    for i in range(5):
        if grid[i][i]==-1: cnt1+=1
        if grid[i][5-i-1]==-1: cnt2+=1
    if cnt1==5: bingo+=1
    if cnt2==5: bingo+=1
    
    # horiz
    for i in range(5):
        if grid[i].count(-1)==5: bingo+=1
    # verti
    for j in range(5):
        cnt3=0
        for i in range(5):
            if grid[i][j]==-1: 
                cnt3+=1
        if cnt3==5: bingo+=1
    if bingo>=3: return True
    else: return False

for i in range(5):
    calls = list(map(int,input().split()))
    for j,call in enumerate(calls):
        remove(call)
        if check():
            print(5*i+j+1)
            exit()