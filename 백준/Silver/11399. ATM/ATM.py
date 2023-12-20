input()
arr = sorted(map(int, input().split()))
ans = [sum(arr[:i]) for i in range(len(arr)+1)]
print(sum(ans))