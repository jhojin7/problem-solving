def matmul(matA,matB):
    ans = []
    for i in range(N):
        ans.append([0 for _ in range(N)])
        for j in range(N):
            for k in range(N):
                ans[i][j] += matA[i][k] * matB[k][j]
    return ans

def matmod(matA,m):
    for i in range(N):
        for j in range(N):
            matA[i][j] %= m
    return matA

def power(b,_m):
    if b == 1:
        return matmod(mat,_m)
    tmp = power(b//2,_m)
    tmptmp = matmul(tmp,tmp)
    if b%2 == 1:
        ret = matmul(tmptmp,mat)
        return matmod(ret,_m)

    else:
        return matmod(tmptmp,_m)
# fibonacci number matrix form + 10830번

mat, N = [[1,1],[1,0]], 2

MOD = 1000000
n = int(input())
print(power(n,MOD)[0][1])