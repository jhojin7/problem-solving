import sys, collections, itertools, heapq, math, re, random
from copy import deepcopy
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

arr = [str('1'*i) for i in range(10000)]
while 1:
    try: 
        n=int(input())
        # print(n,arr[0])
        for x in arr[1:]:
            if int(x)%n==0:
                print(len(x))
                break
    except:
        break