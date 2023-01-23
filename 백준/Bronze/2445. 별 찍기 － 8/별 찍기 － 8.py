N=int(input())
arr = [['*' for _ in range(N*2)] for _ in range(N*2-1)]
# for i in range(N):
#     for j in range(i+1):
#         arr[i][j]='*'
#     for j in range(2*N-1,N-i+3,-1):
#         arr[i][j]='*'

k=1
for i in range(N-2,-1,-1):
    for j in range(N-k,N+k):
        arr[i][j] = ' '
    k+=1


k=1
for i in range(N,2*N-1):
    for j in range(N-k,N+k):
        arr[i][j] = ' '
    k+=1


for row in arr:
    print(*row,sep='')
