import sys, itertools, collections, math, heapq
input = sys.stdin.readline
def intarr(): return list(map(int,input().split()))
def chararr(): return list(input().split())
    # sys.stdout.write("\n")
# ############ CF #######################
for _ in range(int(input())):
    N=int(input())
    for i in range(2,N+10):
        cnt=0
        while N%i==0:
            cnt+=1
            N/=i
        if cnt!=0: print(i,cnt)