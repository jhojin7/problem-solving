N,L,K=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x: (x[1]))
ans=0
# print(arr)
for a,b in arr:
    if K==0: break
    # print((a,b))
    if b<=L and a<=L:
        # print(140)
        ans+=140
    elif not b<=L and a<=L:
        # print(100)
        ans+=100
    else:
        # print("pass")
        K+=1
    K-=1
print(ans)