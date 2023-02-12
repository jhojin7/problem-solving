import sys, collections, heapq, math, re, random
input=sys.stdin.readline

def gcd(m,n):
    while n != 0:
        t = m%n
        (m,n) = (n,t)
    return abs(m)

R,G = map(int,input().split())
# x = min(R,G)
# x = int(math.sqrt(x))
m,n = min(R,G),max(R,G)
x = gcd(m,n)
for i in range(1,x+1):
    if R%i!=0 or G%i!=0: continue
    print(i,R//i,G//i)