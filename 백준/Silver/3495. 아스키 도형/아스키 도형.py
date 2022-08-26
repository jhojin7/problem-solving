h,w = map(int,input().split())
grid = []
for _ in range(h):
    grid.append(list(input().strip()))
# print(grid)

half,full = 0,0
for i in range(h):
    on = False
    for j in range(w):
        # if not on: continue
        if grid[i][j]=='/':
            if on: on = False
            else: on = True
            half+=1
        elif grid[i][j]=='\\':
            if on: on = False
            else: on = True
            half+=1
        elif on and grid[i][j]=='.':
            full+=1
        # print(grid[i][j],on,half,full)
print(half//2+full) 