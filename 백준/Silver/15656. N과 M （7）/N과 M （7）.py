import sys; input = sys.stdin.readline
N,M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

def backtrack(ans):
    if len(ans)==M:
        print(*ans)
        return
    for x in arr:
        ans.append(x)
        backtrack(ans)
        ans.pop()
backtrack([])