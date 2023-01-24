n,k = map(int,input().split())
mod = 1_000_000_007
# nCk %mod
# (n!/(k!(n-k)!))%mod
# (A/B)%mod
# (A%mod)(B^-1%mod)
# (A%mod)((B^mod-2%mod)%mod)

def pow(a,b,mod=1):
    if b==0: return 1
    elif b%2>=1: 
        return (a*pow(a,b-1,mod))
    mid = pow(a,b//2,mod)%mod
    return (mid*mid)%mod

def comb(n,k,mod=1):
    A,B=1,1
    # for i in range(1,n-k):
    for i in range(n,n-k,-1):
        # A*=i%mod
        A = (A*i)%mod
    for i in range(1,k+1):
        # B*=i%mod
        B = (B*i)%mod
    return ((A%mod)*(pow(B,mod-2,mod)))%mod

print(comb(n,k,mod))