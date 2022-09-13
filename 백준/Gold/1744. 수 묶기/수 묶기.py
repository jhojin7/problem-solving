N=int(input())
arr=[]
pos,neg = [],[]
ans=0
for _ in range(N):
    x=int(input())
    # if x==1 or x==0 or x==-1: ans+=x
    # if x==0: continue
    if x>0: pos.append(x)
    elif x<=0: neg.append(x)
pos.sort(reverse=True)
neg.sort()
# print(pos,neg)

while pos:
    a=pos.pop(0)
    if not pos:
        ans+=a
        break
    b=pos.pop(0)
    if a+b>a*b:
        ans+=a+b
    else:
        ans+=a*b

while neg:
    a=neg.pop(0)
    if not neg: 
        ans+=a
        break
    b=neg.pop(0)
    ans+=a*b

print(ans)