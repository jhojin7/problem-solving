import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

M,N = map(int,input().split())
d ={
    0:"zero",1:'one',2:'two',3:'three',4:'four',
    5:'five',6:'six',7:'seven',8:'eight',9:'nine'
}

nums = [i for i in range(M,N+1)]
ans = []
for n in nums:
    if n<10:
        ans.append((d[n],n))
    else:
        a,b = n//10,n%10
        ans.append((' '.join([d[a],d[b]]),n))
ans.sort()

for i in range(len(ans)):
    print(ans[i][1],end=' ')
    if i%10==9: print()