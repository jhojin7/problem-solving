import sys, collections, heapq, math, re, random
input=sys.stdin.readline
def solve(s,t):
    j=0
    for i in range(len(t)):
        if j==len(s): break
        if t[i]==s[j]: j+=1
    if j==len(s):
        print("Yes")
    else: print("No")
while 1:
    try:
        s,t = input().split()
        solve(s,t)
    except: break