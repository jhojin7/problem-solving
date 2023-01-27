import sys,collections, heapq,math, re
input = sys.stdin.readline
# http://boj.kr/608625ed4db742f2b046476a3c958864
# (A/B)%mod
# (A%mod)(B^-1%mod)
# (A%mod)((B^mod-2%mod)%mod)
def pow(a,b,mod=10**100+7):
    if b==0: return 1
    elif b%2>=1: 
        return (a*pow(a,b-1,mod))
    mid = pow(a,b//2,mod)%mod
    return (mid*mid)%mod

mod = 10**9+7
ans=0
for _ in range(int(input())):
    N,S = map(int,input().split())
    # ans+=((S%mod)*pow(N,mod-2,mod))%mod
    ans+=(S*pow(N,mod-2,mod))%mod
print(ans%mod)