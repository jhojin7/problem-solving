""" Shorts """

def q2407():
    """ 2407 조합"""
    def factorial(x):
        if x == 1 or x == 0: return 1
        elif x == 2: return 2
        return factorial(x-1) * x
    # n,m = map(int, input().split())
    n,m = 100, 6
    dp = [1,1,2] 
    for i in range(3,100+1):
        dp.append(dp[i-1]*i)
        # dp[i] = dp[i-1] * i
    print((dp[n]//dp[n-m])//dp[m])

def q25305():
    # https://www.acmicpc.net/source/45174791
    N,k = map(int,input().split())
    scores = sorted(list(map(int,input().split())),reverse=True)
    print(N,k,scores)
    print(scores[k-1])
    pass

# fibonacci https://mortada.net/fibonacci-numbers-in-python.html
# https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
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

def power(b):
    if b == 1:
        return (mat)
    tmp = power(b//2)
    tmptmp = matmul(tmp,tmp)
    if b%2 == 1:
        ret = matmul(tmptmp,mat)
        return (ret)
    else:
        return (tmptmp)

# mat, N = [[1,1],[1,0]], 2
# n = int(input())
# print(power(n)[0][1])


# # 11021
# for i in range(int(input())):
#     a,b = map(int,input().split())
#     print("Case #{}:".format(i+1), a+b)

# # 11720
# https://www.acmicpc.net/source/45582006
n,*s = [*open(0)];S=0
for x in s[0].strip():S+=int(x)
print(S)