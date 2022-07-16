import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [0 for _ in range(N+1)]
tmp = 0
for i in range(1,N+1):
    tmp += A[i-1]
    dp[i] = tmp
# print(dp)

M = int(input())
for _ in range(M):
    i,j = map(int,input().split())
    # print(i,j)
    # i-=1;j-=1;
    print(dp[j]-dp[i-1])