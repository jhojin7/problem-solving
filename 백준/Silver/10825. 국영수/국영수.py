import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    namee,ko,en,mat = input().split()
    arr.append((namee,int(ko),int(en),int(mat)))
arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for x in arr:
    print(x[0])