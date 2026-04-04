ans = []
for i in range(5):
    ans.append(sum(map(int, input().split())))
print(ans.index(max(ans)) + 1, max(ans))