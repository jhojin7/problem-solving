import sys,collections
input = sys.stdin.readline
N=int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
x = list(collections.Counter(arr).items())
x.sort(key=lambda x:(-x[1],x[0]))
# print(x)
print(x[0][0])