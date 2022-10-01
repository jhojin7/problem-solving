N,M,L=map(int,input().split())
if M==1:
    print(0)
    exit()
d = {}
for k in range(N): d[k]=0
cnt=0
k=0
while 1:
    key = k%N
    if d[key]%2==0:
        d[key]+=1
        k+=L
    else:
        d[key]+=1
        k-=L
    if d[key]==M: break
    cnt+=1
print(cnt)