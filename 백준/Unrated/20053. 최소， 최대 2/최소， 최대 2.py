def solve():
    N = int(input())
    arr = list(map(int,input().split()))
    print(min(arr),max(arr))

for _ in range(int(input())):
    solve()