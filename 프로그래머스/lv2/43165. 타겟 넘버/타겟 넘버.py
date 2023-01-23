numbers,target = [],0
cnt=0

def dfs(idx,n):
    global cnt
    if idx==len(numbers):
        if n==target: 
            cnt+=1
        return
    a = dfs(idx+1,n+numbers[idx])
    b = dfs(idx+1,n-numbers[idx])
    return
    
def solution(_numbers, _target):
    global numbers,target
    numbers = _numbers
    target = _target
    dfs(0,0)
    return cnt