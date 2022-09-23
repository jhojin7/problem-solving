n,k=map(int,input().split())
s=0
for _ in range(k):
    s+=int(input())
kk=(n-k)
print((s+(-3)*kk)/n,(s+(3*kk))/n)