N=int(input())
a=[]
for _ in range(N):
    a.append(int(input()))
a.sort(reverse=True)
ans=[]
s=0
for i in range(N):
    if len(ans)==3 and ans[1]+ans[2]>ans[0]:
        break
    if len(ans)==3:
        ans.pop(0)
    x=a[i]
    s+=x
    ans.append(x)

if len(ans)==3 and ans[1]+ans[2]==ans[0]:
    print(-1)
else:
    # print(ans)
    print(sum(ans))