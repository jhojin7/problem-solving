N = int(input())
cows = []
for _ in range(N):
    cows.append(tuple(map(int,input().split())))
cows.sort()
# print(cows)

t = 0
for st,dur in cows:
    if t<st: t = st
    else: t = t
    # print(t)
    t = t+dur
print(t)