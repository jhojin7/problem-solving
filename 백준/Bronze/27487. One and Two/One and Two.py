import sys, collections, heapq, math, re
input=sys.stdin.readline

def solve():
    N=int(input())
    arr = list(map(int,input().split()))
    cnt2 = arr.count(2)
    ans=0
    if cnt2%2==0:
        i=0
        cnt=0
        while i<N:
            if arr[i]==2: cnt+=1
            if cnt==cnt2//2:
                ans=i
                break
            i+=1
        print(ans+1)
    elif cnt2%2!=0:
        print(-1)
for _ in range(int(input())):
    solve()