import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N,M = inputint()
A = [list(inputint()) for _ in range(N)]
M,K = inputint()
B = [list(inputint()) for _ in range(M)]
C = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j]+=\
            A[i][k]*\
            B[k][j]
        
for row in C:
    print(*row)