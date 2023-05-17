import sys; input = sys.stdin.readline
N=int(input())

def backtrack(arr):
    if len(arr)==N:
        print(*arr)
        return
    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            backtrack(arr)
            arr.pop()

for i in range(1,N+1):
    backtrack([i])
