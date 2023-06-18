import sys; input=sys.stdin.readline
import math, itertools

N=int(input())
A = list(map(int, input().split()))
a,b,c,d = list(map(int, input().split()))
signs = []
signs.extend(['+' for _ in range(a)])
signs.extend(['-' for _ in range(b)])
signs.extend(['*' for _ in range(c)])
signs.extend(['/' for _ in range(d)])

perms = itertools.permutations(signs,len(signs))

maxtmp,mintmp = -math.inf, math.inf

for signs in perms:
    tmp = A[0]
    for i,c in enumerate(signs,1):
        if c=='+': tmp += A[i]
        elif c=='-': tmp -= A[i]
        elif c=='*': tmp *= A[i]
        elif c=='/': 
            if tmp < 0:
                tmp = -1*(tmp*-1 // A[i])
            else:
                tmp //= A[i]
    maxtmp = max(maxtmp,tmp)
    mintmp = min(mintmp,tmp)

print(maxtmp)
print(mintmp)