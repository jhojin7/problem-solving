import math
def isprime(n):
    for i in range(2,math.floor(math.sqrt(n))):
        if n%i==0: return False
    return True

while 1:
    p,a = map(int,input().split())
    if p==0 and a==0: break
    # if (not prime[p] 
    #     and (a**p)%p==a):
    if (not isprime(p) 
        and pow(a,p,p)==a):
        print("yes")
    else: print("no")