dic = {
    '.':'.',
    'O':'O',
    '-':'|',
    '|':'-',
    '/':"\\",
    '\\':"/",
    '^':"<",
    '<':"v",
    'v':">",
    '>':"^",
}

N,M=map(int,input().split())
grid = []
for _ in range(N):
    row = list(input().strip())
    grid.append(row)
rotate = [['' for _ in range(M)] for _ in range(N)]
for j in range(M-1,-1,-1):
    for i in range(N):
        print(dic[grid[i][j]],end='')
    print()
