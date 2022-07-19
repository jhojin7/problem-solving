import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    if a>=b: sys.stdout.write("0\n")
    elif b%a!=0: sys.stdout.write("0\n")
    else: sys.stdout.write("1\n")