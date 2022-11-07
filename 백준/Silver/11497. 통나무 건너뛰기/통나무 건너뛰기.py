for _ in range(int(input())):
    N=int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    # fr = arr[:len(arr)//2]
    # re = arr[len(arr)//2:]
    # arr = fr+re[::-1]
    fr,re = [],[]
    for i in range(N):
        if i%2==0: re.append(arr[i])
        else: fr.append(arr[i])
    arr = fr[::-1]+re
    # print(arr)
    diff = 0
    for i in range(N):
        diff = max(diff,abs(arr[(i+1)%N]-arr[i%N]))
    print(diff)