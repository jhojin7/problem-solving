import math
M = 10**9+7
x = 2
ans =0
for _ in range(int(input())):
    c,k = map(int,input().split())
    if c==0 or k==0: continue
    tmp = (c*k)%M * pow(x,k-1,M)
    # print(tmp)
    ans = (ans+tmp)%M
print(ans)