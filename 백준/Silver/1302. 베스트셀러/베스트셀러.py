import sys,collections
input = sys.stdin.readline
N = int(input())
words = []
for _ in range(N):
    word = input().strip()
    words.append(word)
cnter = collections.Counter(words)
common = cnter.most_common(1)[0]
common_cnt = common[1]
arr = []
for k,v in cnter.items():
    if v==common_cnt:
        arr.append(k)
arr.sort()
print(arr[0])