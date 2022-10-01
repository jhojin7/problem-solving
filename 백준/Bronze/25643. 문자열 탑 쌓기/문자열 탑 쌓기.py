N,M = map(int,input().split())
s=input()
ok=True
for _ in range(N-1):
    t=input()
    ok=False
    for k in range(1,M+1):
        # print(s[:k],t[M-k:],s[-k:],t[:k])
        if s[-k:]==t[:k]: ok=True
        if s[:k]==t[M-k:]: ok=True
    # print(ok)
    if not ok: break
    s=t
if ok: print(1)
else: print(0)