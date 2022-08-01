import collections
N = int(input())
arr = list(map(int,input().split()))
cnter = collections.Counter(arr)
M = int(input())
query = list(map(int,input().split()))
for q in query:
    print(cnter[q],end=' ')