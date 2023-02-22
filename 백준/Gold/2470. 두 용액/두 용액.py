import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
A = list(inputint())
A.sort()

l,r = 0,N-1
ans = math.inf
aa,bb = A[l],A[r]
while l<r:
    B = A[l]+A[r]
    # print(A[l],A[r],B)
    if abs(B)<abs(ans):
        ans = B
        aa,bb = A[l],A[r]
    if B<0:
        l+=1
    else:
        r-=1
print(min(aa,bb),max(aa,bb))