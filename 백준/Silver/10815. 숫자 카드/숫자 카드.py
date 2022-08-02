import sys
input = sys.stdin.readline
N=int(input())
arr = set(map(int,input().split()))
M=int(input())
query = list(map(int,input().split()))
# print(arr,query)
for q in query:
    if q in arr:
        sys.stdout.write("1 ")
    else:
        sys.stdout.write("0 ")
