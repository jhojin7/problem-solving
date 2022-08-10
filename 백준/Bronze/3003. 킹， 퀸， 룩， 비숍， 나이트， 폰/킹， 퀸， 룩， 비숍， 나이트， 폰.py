chess=[1,1,2,2,2,8]
arr=list(map(int,input().split()))
ans=[]
for a,b in zip(chess,arr):
    ans.append(a-b)
print(*ans)