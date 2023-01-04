def solve():
    grid = [list(input().strip()) for _ in range(8)]
    totcnt=0
    for row in grid:
        totcnt += row.count('O')
        if row.count('O')>1: return "no"
    for j in range(8):
        cnt=0
        for i in range(8):
            if grid[i][j]=='O': 
                totcnt+=1
                cnt+=1
        if cnt>1: return "no"
    if totcnt!=16: return "no"
    return "yes"

for i in range(1,int(input())+1):
    print(f"#{i} {solve()}")