arr = []
k=int(input())
d=[[] for _ in range(5)]
for _ in range(6):
    a,b = map(int,input().split())
    d[a].append(b)
    arr.append((a,b))
arr.append(arr[0])
direc = [a for a,b in arr]
#13 41 24 32
todel=0
for i in range(len(direc)-1):
    if (direc[i],direc[i+1])==(1,3):
        todel=arr[i][1]*arr[i+1][1]
    elif (direc[i],direc[i+1])==(4,1):
        todel=arr[i][1]*arr[i+1][1]
    elif (direc[i],direc[i+1])==(2,4):
        todel=arr[i][1]*arr[i+1][1]
    elif (direc[i],direc[i+1])==(3,2):
        todel=arr[i][1]*arr[i+1][1]

tmp=[]
for i in range(1,5):
    if len(d[i])==1:tmp.append(max(d[i]))
total=tmp[0]*tmp[1]
print(k*(total-todel))
