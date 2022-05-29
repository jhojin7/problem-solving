"""
https://www.acmicpc.net/problem/1065
https://www.acmicpc.net/source/43934767
"""
N = 1
cnt = N
for n in range(1,N+1):
    li = (list(str(n)))
    # numbers 1~99 are all 한수
    if 1<=n<=99: 
        continue
    # set diff as difference between first and second value
    diff = (int(li[0])-int(li[1]))
    # loop from third value to end
    for i in range(2,len(li)):
        # if diff between previous value and current value
        # is different from diff, then n isnt 한수 
        new_diff = (int(li[i-1])-int(li[i]))
        if new_diff != diff:
            # subtract from N
            cnt -= 1
            break
    #     else: 
    #         print(n,diff, cnt)
    # print(n,cnt)
print(cnt)