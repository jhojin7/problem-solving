import sys,collections
input = sys.stdin.readline
n,c = map(int,input().split())
nums = list(map(int,input().split()))
cnter = collections.Counter(nums)
cnter = sorted(cnter.items(),key=lambda x:(-x[1]))
for cnt in cnter:
    for _ in range(cnt[1]):
        print(cnt[0],end=' ')