import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N=int(input())
A = list(inputint())
# print(A)
if len(A)==2:
    print(sum(A))
    exit()

l,r = 0,N-1
ans = math.inf
while l<r:
    B = A[l]+A[r]
    # print(A[l],A[r],B)
    if abs(B)<abs(ans):
        ans = B
    if B<0:
        l+=1
    else:
        r-=1
print(ans)