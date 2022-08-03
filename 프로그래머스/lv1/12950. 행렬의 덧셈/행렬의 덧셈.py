def solution(arr1, arr2):
    N=len(arr1)
    M=len(arr1[0])
    ans = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            ans[i][j] = arr1[i][j]+arr2[i][j]
    return ans