# unsolved... 33.3/100

import random
def solution(numbers):
    max_ans = 0
    for _ in range(1000):
        arr = random.sample(numbers,len(numbers))
        joined = int(''.join([str(x) for x in arr]))
        if max_ans < joined:
            max_ans = joined
    return str(max_ans)
print(solution([6,10,2]))
print(solution([3,30,34,5,9]))