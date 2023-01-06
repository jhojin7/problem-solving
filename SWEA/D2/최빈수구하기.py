import collections, itertools, heapq

def solve():
    N = int(input())
    arr = list(map(int,input().split()))
    return collections.Counter(arr).most_common(1)[0][0]

# for i in range(1,11):
for i in range(1,int(input())+1):
    print(f"#{i} {solve()}")
