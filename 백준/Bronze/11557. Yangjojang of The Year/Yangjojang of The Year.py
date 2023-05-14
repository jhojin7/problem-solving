import sys; input = sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    arr = []
    for _ in range(N):
        S,L = input().split()
        arr.append((S,int(L)))
    arr.sort(key = lambda x:-x[1])
    print(arr[0][0])