N=int(input())
d={}
for i in range(N):
    s=input()
    d[s]=i
# print(d)
arr=[]
for i in range(N):
    s=input()
    arr.append(d[s])
cnt=0
for i in range(N):
    for j in range(i+1,N):
        if i<j and arr[i]>arr[j]:
            cnt+=1
            break
print(cnt)