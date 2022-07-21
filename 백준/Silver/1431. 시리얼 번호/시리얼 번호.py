import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    str = input().strip()
    numsum = 0
    for c in str:
        if c in "1234567890":
            numsum += int(c)
    tup = (len(str),numsum,str)
    arr.append(tup)
arr.sort()

for tup in arr:
    print(tup[2])