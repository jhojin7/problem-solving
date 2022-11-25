import collections
def solution(k, tangerine):
    cnter = sorted(collections.Counter(tangerine).items(),
                  key=lambda x:(-x[1],x[0]))
    cnt, ans=0,0
    for _,v in cnter:
        cnt+=v
        ans+=1
        if cnt>=k:
            return ans