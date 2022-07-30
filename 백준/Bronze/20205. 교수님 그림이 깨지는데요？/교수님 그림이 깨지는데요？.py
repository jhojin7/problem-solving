N,K = map(int,input().split())
grid = []
for _ in range(N):
    row = list(input().split())
    grid.append(row)

for i in range(N*K):
    for j in range(N*K):
        print(grid[i//K][j//K],end=' ')
    print()