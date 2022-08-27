import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    print(min(a,b,c))