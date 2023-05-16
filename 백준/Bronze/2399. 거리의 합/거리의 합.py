import sys; input = sys.stdin.readline
n=int(input())
arr = list(map(int,input().split()))
ans =0
for x in arr:
    for y in arr:
        ans+=abs(x-y)
print(ans)