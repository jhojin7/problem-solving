arr=['N']+list(input().strip())
# print(arr)
cnt=0
for i in range(1,len(arr)):
    if arr[i]=='N': continue
    ok=False
    for j in range(i,len(arr),i):
        ok=True
        if arr[j]=='Y': arr[j]='N'
        else: arr[j]='Y'
    if ok: cnt+=1
# print(arr)
if 'Y' in arr: print(-1)
else: print(cnt)