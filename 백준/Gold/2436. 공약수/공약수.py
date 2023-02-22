import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return abs(a)
def lcm(a,b):
    return a*b//gcd(a,b)

G,L = inputint()
ab = L//G
# print(ab)
aa,bb =0,0
for a in range(1,int(math.sqrt(ab))+1):
    if ab%a!=0: continue
    b = ab//a
    if gcd(a,b)!=1: continue
    # print(a*G,b*G,G*(a+b))
    aa,bb = a*G,b*G
print(aa,bb)