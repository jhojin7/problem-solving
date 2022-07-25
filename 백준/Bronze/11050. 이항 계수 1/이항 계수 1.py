def facto(x):
    ret = 1
    for i in range(1,x+1):
        ret *= i
    return ret

def comb(n,k):
    return facto(n)//(facto(n-k)*facto(k))

a,b = map(int,input().split())
print(comb(a,b))