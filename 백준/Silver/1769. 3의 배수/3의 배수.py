X=input().strip()
cnt=0
# print(X)
while len(X)>1:
    cnt+=1
    X=list(map(int,X.strip()))
    # print(X)
    X=str(sum(X))
print(cnt)
if X in "369": print("YES")
else: print("NO")