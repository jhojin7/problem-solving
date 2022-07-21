import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    word = input().strip()
    if word not in arr:
        arr.append(word)
arr.sort(key=lambda x:(len(x),x))
for word in arr: print(word)