def solution(arr):
    i=0
    ans = []
    while i<len(arr):
        j = i+1
        ans.append(arr[i])
        while j<len(arr) and arr[i]==arr[j]:
            j+=1
        i=j
    return ans
