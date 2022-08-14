def f(n):
    cnt = 0
    for i in range(1,n-1+1): 
        cnt += n-i
    return cnt

n = int(input())
ans = f(n)
print(ans)
print(2)