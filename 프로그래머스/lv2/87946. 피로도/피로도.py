import itertools
def solution(k,dungeons):
    n=len(dungeons)
    perms = itertools.permutations(range(0,n),n)
    ans = 0
    for perm in perms:
        kk = k
        cnt =0
        for i in perm:
            if kk>=dungeons[i][0]:
                kk-=dungeons[i][1]
                cnt+=1
            ans = max(ans,cnt)
    return ans