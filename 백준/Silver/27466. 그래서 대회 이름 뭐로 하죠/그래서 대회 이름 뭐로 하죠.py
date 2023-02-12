import sys, collections, heapq, math, re, random
input=sys.stdin.readline

N,M = map(int,input().split())
S = input().strip()
ans=collections.deque()
if S[-1] not in "AEIOU":
    ans.appendleft(S[-1])
if M==0:
    print("NO")
    exit()
Acnt=0
ii=0
for i in range(N-2,-1,-1):
    if len(ans)==M:
        break
    if S[i]=='A': 
        ans.appendleft(S[i])
        Acnt+=1
    if Acnt==2:
        ii=i
        break
for i in range(ii-1,-1,-1):
    if len(ans)==M:
        break
    ans.appendleft(S[i])

if len(ans)!=M:
    print("NO")
else:
    print("YES")
    print(''.join(ans))
