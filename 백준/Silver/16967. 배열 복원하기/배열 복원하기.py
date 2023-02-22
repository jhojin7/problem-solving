import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

H,W,X,Y = inputint()
B = [list(inputint()) for _ in range(H+X)]
# print(B)
A = [[B[i][j] for j in range(W)] for i in range(H)]
# print(A)

for i in range(X,H):
    for j in range(Y,W):
        # print(A[i][j],B[i+X][j+Y])
        A[i][j] = (A[i][j]-A[i-X][j-Y])
        # A[i][j] = B[i+X][j+Y]

for a in A:
    print(*a)