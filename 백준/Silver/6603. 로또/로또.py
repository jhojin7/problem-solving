import sys,itertools
input = sys.stdin.readline

while True:
    k = input().strip()
    if k=="0": break
    k,*S = map(int,k.split())
    ans = itertools.combinations(S,6)
    for x in ans:
        print(*x)
    print()