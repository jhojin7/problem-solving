import sys; input = sys.stdin.readline
N,K = map(int,input().split())
arr = list(input().strip())
for i in range(N):
    if arr[i]=='P':
        for j in range(i-K,i+K+1):
            if 0<=j<N and arr[j] == 'H':
                arr[j] = '.'
                break
print(arr.count('.'))