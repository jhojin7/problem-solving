"""
id: 10830
title:행렬제곱
ac:https://www.acmicpc.net/source/44929323 
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2 1
1000 1000
1000 1000
""".strip())

def matmul(matA,matB):
    ans = []
    for i in range(N):
        ans.append([0 for _ in range(N)])
        for j in range(N):
            # ans[i][j] %= 1000
            for k in range(N):
                # print((i,k),(k,j))
                ans[i][j] += matA[i][k] * matB[k][j]
    return ans

def matmod(matA,m):
    for i in range(N):
        for j in range(N):
            matA[i][j] %= m
    return matA

def power(b):
    if b == 1:
        return matmod(mat,1000)
    tmp = power(b//2)
    if b%2 == 1:
        tmptmp = matmul(tmp,tmp)
        ret = matmul(tmptmp,mat)
        return matmod(ret,1000)
    else:
        tmptmp = matmul(tmp,tmp)
        return matmod(tmptmp,1000)

import sys
N,B = map(int,input().split())
mat = []
for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    mat.append(row)
ans = power(B)
for i in range(N):
    print(*ans[i],sep=' ')