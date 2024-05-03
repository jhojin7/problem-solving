def solution(s):
    d = {}
    ans = []
    for i,c in enumerate(s):
        if c not in d.keys():
            d[c] = i
            ans.append(-1)
        else:
            ans.append(i-d[c])
            d[c] = i
    return ans 
