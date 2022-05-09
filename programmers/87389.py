def solution(n):
    # n%x==1
    for x in range(1,n):
        if n%x==1: return x
print(solution(10))