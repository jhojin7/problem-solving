import collections
def solution(clothes):
    d = collections.defaultdict(list)
    for v,k in clothes:
        d[k].append(v)
    ans = 1
    for k,v in d.items():
        ans*=len(v)+1
    print(ans-1,d)
    return ans-1