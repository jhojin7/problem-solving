N,S,R = map(int,input().split())
no=list(map(int,input().split()))
extra=list(map(int,input().split()))
kayak = [1 for _ in range(N+1)]
kayak[0]=9999

for i in range(1,N+1):
    if i in no:
        kayak[i]-=1
    if i in extra:
        kayak[i]+=1
# print(kayak)
k1 = kayak.copy()
k2 = kayak.copy()
for i in range(N,1,-1):
    if k1[i]!=0: continue
    if k1[i-1]==2:
        k1[i-1]-=1
        k1[i]+=1
# print(k1)
# print(kayak)
for i in range(1,N):
    if k2[i]!=0: continue
    if k2[i+1]==2:
        k2[i+1]-=1
        k2[i]+=1
# print(k2)
print(min(kayak.count(0),k1.count(0),k2.count(0)))