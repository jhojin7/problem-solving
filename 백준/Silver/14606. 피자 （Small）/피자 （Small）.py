import sys, collections, heapq, math, re
N=int(input())

if N==1: 
    print(0)
    exit()
print(N*(N-1)//2)