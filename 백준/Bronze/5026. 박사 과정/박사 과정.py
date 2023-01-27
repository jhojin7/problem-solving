import sys,collections, heapq,math
input = sys.stdin.readline

N=int(input())
for _ in range(N):
    s=input()
    if s=="P=NP\n": print("skipped")
    else: print(eval(s))