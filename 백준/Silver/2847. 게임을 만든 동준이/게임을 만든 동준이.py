N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))
M = arr[-1]-1
cnt=0
for i in range(N-2,-1,-1):
    cur = arr[i]
    if cur<M:
        M=cur-1
        continue
    else:
        cnt+=abs(M-cur)
        arr[i] = M
        M-=1
    # print(arr,cnt)
print(cnt)