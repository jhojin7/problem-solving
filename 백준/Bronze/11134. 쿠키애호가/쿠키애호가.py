import sys; input = sys.stdin.readline

for _ in range(int(input())):
    N,C = map(int,input().split())
    ans = N//C
    ans+=1 if N%C!=0 else 0
    print(ans)