import math
# c_i = c mod m_i
# 0<=c<=prod(M)
arr = list(map(int,input().split()))
C = arr[3:]
M = arr[:3]
ans = []
for c in range(math.prod(M)):
    ok = True
    for c_i,m_i in zip(C,M):
        if not c_i == c % m_i:
            ok=False
    if ok:
        ans.append(c)
if len(ans)==0:
    print(-1)
else:
    print(min(ans))