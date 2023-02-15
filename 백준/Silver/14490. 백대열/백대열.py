import sys, collections, heapq, math, re, random
input=sys.stdin.readline

n,m = map(int,input().split(':'))
g = math.gcd(n,m)
print(f"{n//g}:{m//g}")