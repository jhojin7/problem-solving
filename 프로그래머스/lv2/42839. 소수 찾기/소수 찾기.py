def isprime(n):
    if n==0: return False
    if n==1: return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

import itertools
def solution(numbers):
    ans = set()
    for r in range(1,len(numbers)+1):
        comb = list(itertools.permutations(numbers,r))
        for c in comb:
            x = int(''.join(c))
            if isprime(x): ans.add(x)
    return len(ans)