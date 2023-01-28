import sys, collections, heapq, math, re
input = sys.stdin.readline

def pow(a,b,mod=10**9+7):
    if b==0: return 1
    elif b%2>=1: 
        return (a*pow(a,b-1,mod))
    mid = pow(a,b>>1,mod)%mod
    return (mid*mid)%mod

def comb(n,k,mod=10**9+7):
    # http://boj.kr/608625ed4db742f2b046476a3c958864
    A,B=1,1
    for i in range(n,n-k,-1):
        A = (A*i)%mod
    for i in range(1,k+1):
        B = (B*i)%mod
    return ((A%mod)*(pow(B,mod-2,mod)))%mod

M=int(input())
mod = 10**9+7

# factorials
factorials = [0 for _ in range(400_001)]
factorials[0] = 1
for i in range(1,400_001):
    factorials[i] = (factorials[i-1]*i)%mod
# inverse
inverse = [0 for _ in range(400_001)]
inverse[400_000] = pow(factorials[400_000],mod-2,mod)
for i in range(400_000-1,-1,-1):
    inverse[i] = (inverse[i+1]*(i+1))%mod

ans=0
for n in range(3,M+1):
    # ans = (ans + comb(2*n,n,mod))%mod
    nn,kk = 2*n,n
    x=(factorials[nn]*inverse[nn-kk])%mod
    x = (x*inverse[kk])%mod
    ans+= x%mod
print(ans%mod)

# 3 20
# 4 90
# 100 171282861