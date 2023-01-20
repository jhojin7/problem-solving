N=int(input())
arr = [['' for _ in range(N)]
        for _ in range(N*2)]
on=True
for i in range(N*2):
    if i%2==0: on=True
    else: on=False
    for j in range(N):
        arr[i][j] = '*' if on else ' '
        on = False if on else True
for i in range(N*2):
    for j in range(N):
        if j==N-1 and arr[i][j]==' ':
            continue
        print(arr[i][j],end='')
    print()