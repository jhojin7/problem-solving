def gcd(a,b):
    ans = 0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            ans = i
    return ans
def lcm(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            return i
a,b=map(int,input().split())
print(gcd(a,b))
print(lcm(a,b))