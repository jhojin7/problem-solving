import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N = int(input())
M = int(input())
S = collections.deque(inputchars())

i = 0
ioi = 0
ans = 0
while i<len(S)-2:
    IOI = [S[i],S[i+1],S[i+2]]
    # print(ioi,IOI)
    if ''.join(IOI)=="IOI":
        ioi+=1
        i+=2
        if ioi==N:
            ans+=1
            ioi-=1
            # print(ans)
    else:
        i+=1
        ioi=0
print(ans)