import sys; input = sys.stdin.readline
N,M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

def backtrack(ans,i):
    if len(ans)==M:
        print(*ans)
        return
    for j in range(i,N):
        ans.append(arr[j])
        backtrack(ans,j+1)
        ans.pop()
backtrack([],0)