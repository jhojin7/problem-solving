N = int(input())
S = input()
D, M = map(int, input().split())
h = S.count('H')
y = S.count('Y')
u = S.count('U')
S = S.replace('H', ' ')
S = S.replace('Y', ' ')
S = S.replace('U', ' ')
ans = 0
for s in S.split():
    ans += min(D+M, D*len(s))

if ans == 0:
    print("Nalmeok")
else:
    print(ans)
if min(h, y, u) == 0:
    print("I love HanYang University")
else:
    print(min(h, y, u))
