import collections, math, sys, itertools,heapq
input = sys.stdin.readline
for _ in range(int(input())):
    s=input().strip()
    ends=s[-2:]
    if s[-1]=="a": s=s[:-1]+"as"
    elif s[-1]=="i": s=s[:-1]+"ios"
    elif s[-1]=="y": s=s[:-1]+"ios"
    elif s[-1]=="l": s=s[:-1]+"les"
    elif s[-1]=="n": s=s[:-1]+"anes"
    elif s[-2:]=="ne": s=s[:-2]+"anes"
    elif s[-1]=="o": s=s[:-1]+"os"
    elif s[-1]=="r": s=s[:-1]+"res"
    elif s[-1]=="t": s=s[:-1]+"tas"
    elif s[-1]=="u": s=s[:-1]+"us"
    elif s[-1]=="v": s=s[:-1]+"ves"
    elif s[-1]=="w": s=s[:-1]+"was"
    else: s=s+"us"
    print(s)