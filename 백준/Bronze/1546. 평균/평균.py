N = int(input())
arr = list(map(int,input().split()))
curavg = sum(arr)/len(arr)
M = max(arr)
newarr = [a/M*100 for a in arr]
newavg = sum(newarr)/len(newarr)
print(newavg)