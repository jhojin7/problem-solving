def calc(stones,mid, k):
    cnt = 0
    for stone in stones:
        if stone-mid <=0:
            cnt+=1
        else:
            cnt =0
        if cnt==k:
            return False
    return True

def solution(stones, k):
    N = len(stones)
    start, end = 0,200_000_000

    while start< end:
        mid = (start+end)//2
        res = calc(stones, mid, k)
        print(start, end, mid, res)
        if res:
            start = mid+1
        else:
            end = mid
        
    return start