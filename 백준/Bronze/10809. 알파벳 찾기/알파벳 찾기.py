s=input()
alpha = "abcdefghijklmnopqrstuvwxyz"
arr=[-1 for _ in range(26)]
for i,c in enumerate(s): 
    idx = alpha.index(c)
    # print(i,idx)
    if arr[idx] == -1:
        arr[idx] = i
print(*arr)