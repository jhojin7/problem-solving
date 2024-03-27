for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    ans =0
    m = arr[-1]
    for i in range(N-1,-1,-1):
        if m<arr[i]:
            m = arr[i]
        else:
            ans += m-arr[i]
    print(ans)