def solve():
    N = int(input())
    ans =0
    arr = list(map(int,input().split()))
    for i in range(2,len(arr)-2):
        diff = arr[i]-max(arr[i-2],arr[i-1],arr[i+1],arr[i+2])
        if diff>=0: ans+=diff
    return ans
for i in range(1,11):
    print(f"#{i} {solve()}")
