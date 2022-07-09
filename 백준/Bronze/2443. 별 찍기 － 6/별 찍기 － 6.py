import sys
input = sys.stdin.readline
N = int(input())
for i in range(N,0,-1):
    for _ in range(N-(2*i)//2):
        sys.stdout.write(" ")
    for _ in range(2*i-1):
        sys.stdout.write("*")
    print()