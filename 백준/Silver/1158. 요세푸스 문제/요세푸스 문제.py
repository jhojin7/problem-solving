import sys
input = sys.stdin.readline
N,K = map(int,input().split())
circle = [i for i in range(1,N+1)]
ans =[]
idx = K-1
while len(circle)>0:
    x = circle.pop(idx)
    ans.append(x)
    if len(circle) == 0: break
    idx = (idx+K-1)%len(circle)
    # print(idx,circle[idx])
out = ", ".join(map(str,ans))
print("<"+out+">")