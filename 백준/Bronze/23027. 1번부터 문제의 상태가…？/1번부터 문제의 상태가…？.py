import sys, collections, heapq, math, re

arr=list(input().strip())
f1,f2,f3,f4=False,False,False,False
if 'A' in arr: 
    for i in range(len(arr)):
        if arr[i] in "BCDF":
            arr[i]='A'
elif ('A' not in arr
        and 'B' in arr): 
    for i in range(len(arr)):
        if arr[i] in "CDF":
            arr[i]='B'
elif ('A' not in arr
    and 'B' not in arr
    and 'C' in arr): 
    for i in range(len(arr)):
        if arr[i] in "DF":
            arr[i]='C'
elif ('A' not in arr
    and 'B' not in arr
    and 'C' not in arr): 
    print('A'*len(arr))
    exit()
print(''.join(arr))