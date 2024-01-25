H, W = map(int, input().split())
arr = list(map(int, input().split()))
grid = [[0 for _ in range(W)] for _ in range(H)]
for j in range(W):
    for i in range(arr[j]):
        grid[i][j] = 1

for i in range(H):
    for j in range(W):
        if grid[i][j] in [1, 2]:
            continue
        yes1 = False
        yes2 = False
        for k in range(j, W):
            if grid[i][k] == 1:
                yes1 = True
        for k in range(j, -1, -1):
            if grid[i][k] == 1:
                yes2 = True
        if yes1 and yes2:
            grid[i][j] = 2


print(sum([row.count(2) for row in grid]))
