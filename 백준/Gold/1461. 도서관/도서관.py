import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N,M = map(int,input().split())
arr = list(map(int,input().split()))
# arr.sort(key=lambda x:abs(x))
pos,neg = [],[]
for a in arr:
    if a>0:pos.append(a)
    else:neg.append(a)
pos.sort(); neg.sort(reverse=True);

# # print(sum([2,2,6,6,11,11,28,1,29,37,2]))
# # print(sum([18,18,22,22,26,26,40,40,45,45,50]))
# # print(sum([18,18,45,45,50]))
# print(sum([11,11,6,6,29,29,39]))
# # print(sum([18,18,50,50,45]))
# print(sum([45,45,9,9,50]))
# print(sum([1,1,3,3,5,5,11]))

ans = 0
# init
if pos and neg and pos[-1]<abs(neg[-1]):
    if neg:
        ans+=abs(neg[-1])
        for _ in range(M): 
            if neg: neg.pop()
            else: break
else:
    if pos:
        ans+=pos[-1]
        for _ in range(M): 
            if pos: pos.pop()
            else:break
    else:
        ans+=abs(neg[-1])
        for _ in range(M): 
            if neg: neg.pop()
            else: break

# print(neg,pos,ans)
while neg:
    ans+=abs(neg[-1])*2
    for _ in range(M): 
        if neg: neg.pop()
        else: break
    # print(neg,pos,ans)
while pos:
    ans+=abs(pos[-1])*2
    for _ in range(M): 
        if pos: pos.pop()
        else: break
    # print(neg,pos,ans)
print(ans)