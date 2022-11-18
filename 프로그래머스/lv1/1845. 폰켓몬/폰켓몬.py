import collections
def solution(nums):
    N = len(nums)
    cnter = collections.Counter(nums)
    cnter = sorted(cnter.items(),key=lambda x:x[1])
    print(cnter)
    half = N//2
    cnt = 0
    for i in range(len(cnter)):
        if half==0:
            return cnt
        if cnter[i][1] >0:
            #cnter[i][1]-=1
            half-=1
            cnt+=1
        else:
            continue
    return cnt
        
        