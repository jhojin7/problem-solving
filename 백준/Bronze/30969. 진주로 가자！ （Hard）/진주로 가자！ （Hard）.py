import collections
N = int(input())
# cnt = collections.defaultdict(int)
cnt = [0 for _ in range(1001)]
j = 0
other = 0
for _ in range(N):
    a, b = input().split()
    b = int(b)
    if b <= 1000:
        cnt[b] += 1
    else:
        other += 1
    if a == "jinju":
        j = b
print(j)
print(other+sum(cnt[j+1:]))
