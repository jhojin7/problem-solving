import math
while 1:
    n,k = map(int,input().split())
    if n==k==0:
        break
    print(math.comb(n,k))