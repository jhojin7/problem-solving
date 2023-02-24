import math

def solve():
    N = int(input())
    arr = list(map(int,input().split()))
    i =0
    maxsum = -math.inf
    for i in range(N):
        for j in range(i+1,N+1):
            tmp = sum(arr[i:j])
            if tmp>=maxsum:
                maxsum=tmp
    print(maxsum)

for _ in range(int(input())):
    solve()