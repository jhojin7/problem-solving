import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N = int(input())
arr = list(inputint())
d = collections.defaultdict(list)
# arr.sort()
# print(arr)
for n in range(1,20_001):
    s=0
    for a in arr:
        s+=abs(n-a)
    # d[s]=min(n,d[s])
    d[s].append(n)
    # if s in d.keys():
    #     d[s]=min(n,d[s])
    # else:
    #     d[s] = n
# print(d)
print(min(d[min(d.keys())]))