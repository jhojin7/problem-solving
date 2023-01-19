import sys; input=sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
ans=0
for a in A:
    x=a-B
    ans+=1
    if x>0:
        r = 1 if x%C!=0 else 0
        ans+=(x//C)+r
        # while x>0:
        #     x-=C
        #     ans+=1
print(ans)