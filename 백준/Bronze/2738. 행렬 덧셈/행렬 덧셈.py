import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A,B,C = [],[],[]

for _ in range(N):
    row = list(map(int,input().split()))
    A.append(row)
for _ in range(N):
    row = list(map(int,input().split()))
    B.append(row)
for i in range(N):
    C.append([0 for _ in range(M)])
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
# print(C)
for i in range(N):
    for j in range(M):
        print(C[i][j],end=' ')
    print()