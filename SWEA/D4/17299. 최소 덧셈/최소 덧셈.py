import math
for t in range(int(input())):
    s = input().strip()
    ans = math.inf
    for i in range(1,len(s)):
        ss = int(''.join(s[:i])) + int(''.join(s[i:]))
        ans = min(ans,ss)
    print(f"#{t+1} {ans}")
