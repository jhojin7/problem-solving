import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

word = input().strip()
"""
abbabbbb
a bba bbbb
a abb bbbb
"""
N = len(word)
ans = []
for i in range(1,N):
    for j in range(i+1,N):
        if i==j: continue
        a,b,c = word[:i],word[i:j],word[j:]
        a=a[::-1]
        b=b[::-1]
        c=c[::-1]
        # print(a,b,c)
        ans.append(''.join([a,b,c]))
ans.sort()
print(ans[0])