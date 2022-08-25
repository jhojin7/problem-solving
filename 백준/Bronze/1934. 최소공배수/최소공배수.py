def gcd(a,b):
    a,b = max(a,b),min(a,b)
    r = a%b
    while b!=0:
        r = a%b
        a,b = b,r
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(lcm(a,b))