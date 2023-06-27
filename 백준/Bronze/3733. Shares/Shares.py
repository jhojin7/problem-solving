import sys; input = sys.stdin.readline
import heapq, collections, itertools, math

while 1:
    try: N,S = map(int,input().split())
    except: break
    print(S//(N+1))