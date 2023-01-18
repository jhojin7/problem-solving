arr = [list(map(int,input().split())) for _ in range(9)]
ans = 0
ii,jj = 0,0
for i in range(9):
    for j in range(9):
        if arr[i][j]>ans:
            ans=arr[i][j]
            ii,jj = i,j
print(ans)
print(ii+1,jj+1)