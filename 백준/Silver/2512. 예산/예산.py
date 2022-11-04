N=int(input())
arr = list(map(int,input().split()))
arr.sort()
M = int(input())
if M >= sum(arr):
    print(max(arr))
    exit()
l,r = 1,max(arr)
while l<=r:
    m = (l+r)//2
    tmp = 0
    for a in arr:
        if a>m: tmp += m
        else: tmp+= a
    # print(m, tmp, M)
    if tmp <= M: 
        ans = m
        l = m+1
    else: r = m-1
print(ans)