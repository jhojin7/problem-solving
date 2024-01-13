N = int(input())
s = input()

s = list(s.replace("long", ".").strip())
N = len(s)
dp = [0 for _ in range(100)]
dp[0] = dp[1] = 1
for i in range(2, 100):
    dp[i] = dp[i-1]+dp[i-2]

ans = 1
tmp = []
i = 0
while i < N:
    # print(tmp, ans)
    if s[i] == '.':
        tmp.append(s[i])
        i += 1
        continue
    else:
        # print(tmp)
        if len(tmp) > 0:
            ans *= dp[len(tmp)]
        tmp = []
    i += 1
if len(tmp) > 0:
    ans *= dp[len(tmp)]
print(ans)
