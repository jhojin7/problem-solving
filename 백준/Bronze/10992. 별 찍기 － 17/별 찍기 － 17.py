N=int(input())
arr = [[' ' for _ in range(N*2-1)] for _ in range(N)]
mid = N-1
for i in range(N-1):
    arr[i][mid-i] = '*'
    arr[i][mid+i] = '*'
    for j in range(mid+i+1,2*N-1):
        arr[i][j] = ''
arr[-1] = ['*' for _ in range(2*N-1)]
for i in arr:
    print(*i,sep='')