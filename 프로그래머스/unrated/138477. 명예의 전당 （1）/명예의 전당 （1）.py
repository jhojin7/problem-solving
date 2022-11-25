def solution(k, score):
    arr, ans = [], []
    for i,s in enumerate(score):
        arr.append(s)
        if i<k:
            ans.append(sorted(arr,reverse=True)[i])
        else:
            ans.append(sorted(arr,reverse=True)[k-1])
    return ans
