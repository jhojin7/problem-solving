for _ in range(int(input())):
    N=int(input())
    arr=list(map(int,input().split()))
    profit=0
    M = arr[-1]
    for i in range(N-1,-1,-1):
        if arr[i]>M:
            # update max
            M=arr[i]
        else:
            # add profit
            profit+=M-arr[i]
        # print(M,profit)
    print(profit)

# https://www.acmicpc.net/board/view/16527
# 뒤에서부터-> 커지면 최고값 갱신, 작아지면 그 차이를 이득으로.