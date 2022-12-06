import sys
alpha = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans =0
arr = sys.stdin.readlines()
for i,s in enumerate(arr):
    arr[i] = set(s.strip())
brr = []
for i in range(0,len(arr),3):
    sss = arr[i].intersection(arr[i+1].intersection(arr[i+2]))
    print(sss)
    brr.append(sss)
for s in brr:
    ans+=alpha.index(s.pop())
print(ans)

# for s in arr:
#     s = s.strip()
#     s1,s2 = s[:len(s)//2],s[len(s)//2:]
#     s1,s2 = set(s1.strip()),set(s2.strip())
#     ss = s1.intersection(s2).pop()
#     ans+=alpha.index(ss)
# print(ans)