for i in range(1,int(input())+1):
    arr = list(map(int,input().split()))
    ans=0
    if sum(arr)%len(arr)>5: ans+=1
    ans += sum(arr)//len(arr)
    print(f"#{i} {ans}")