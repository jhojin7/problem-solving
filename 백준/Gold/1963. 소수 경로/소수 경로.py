import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

nums = [True for _ in range(10001)]
nums[1] = False

for i in range(2,10001):
    if not nums[i]: continue
    for j in range(i*2,10001,i):
        nums[j]= False

def solve():
    A,B = map(int,input().split())
    if A==B:
        print(0)
        return
    
    q = collections.deque([(A,0)])
    vis = set()
    while q:
        n,cnt = q.popleft()
        if n==B:
            print(cnt)
            return
        if n in vis: continue
        vis.add(n)
        nxt = []
        nxt.extend([n//10*10+i for i in range(0,10)])
        n2 = n//100*100+n%10
        nxt.extend([n2+10*i for i in range(0,10)])
        n3 = n//1000*1000+n%100
        nxt.extend([n3+100*i for i in range(0,10)])
        nxt.extend([n%1000+1000*i for i in range(0,10)])
        for nx in nxt:
            if nums[nx] and 1000<=nx<=9999: 
                q.append((nx,cnt+1))
    print("Impossible")

for _ in range(int(input())):
    solve()