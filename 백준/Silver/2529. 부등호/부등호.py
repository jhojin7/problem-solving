import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline

k=int(input())
arr = input().split()

gans = []
def dfs(idx,ans=[]):
    if idx==k:
        aaa = (''.join(map(str,ans)))
        gans.append(aaa)
        return
    for nxt in range(0,10):
        if arr[idx]=='<' and ans[-1]>nxt: continue
        if arr[idx]=='>' and ans[-1]<nxt: continue
        if nxt in ans: continue
        dfs(idx+1,ans+[nxt])
    return

for xx in range(0,10):
    dfs(0,[xx])
print(max(gans))
print(min(gans))