import sys; input = sys.stdin.readline
import heapq, collections, itertools

# https://www.acmicpc.net/source/56302495
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return abs(a)
def lcm(a,b):
    return a*b//gcd(a,b)

a,b = map(int,input().split())
a,b = min(a,b), max(a,b)
print(lcm(a,b))
