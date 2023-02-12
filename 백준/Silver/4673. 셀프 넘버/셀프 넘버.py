import sys, collections, heapq, math, re, random
input=sys.stdin.readline


nums = [i for i in range(50001)]
def d(n):
    ret = n
    while n:
        ret+=n%10
        n//=10
    return ret
for n in range(1,10001):
    nums[d(n)]=n
ans=0
for n in range(1,10001):
    if nums[n]==n:
        print(n)