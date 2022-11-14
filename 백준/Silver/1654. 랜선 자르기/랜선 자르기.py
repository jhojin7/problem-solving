K,N = map(int,input().split())
arr = [int(input()) for _ in range(K)]
# print(arr)
l,r = 1,max(arr)
while l<=r:
    m = (l+r)//2
    cnt = 0
    for a in arr:
        cnt+=a//m
    if cnt>=N:
        l = m+1
    else:
        r = m-1
print(r)