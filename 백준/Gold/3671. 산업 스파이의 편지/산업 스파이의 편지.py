import itertools
import math

def solution(numbers):
    ans = set()
    for r in range(1,len(numbers)+1):
        comb = list(itertools.permutations(numbers,r))
        for c in comb:
            x = int(''.join(c))
            if nums[x]: ans.add(x) 
    print(len(ans))

N = 10000003
M = math.ceil(math.sqrt(N))
nums = [True for _ in range(N)]
nums[0] = False
nums[1] = False
for i in range(2,M):
    if not nums[i]: continue
    for j in range(i*i,N,i):
        if not nums[j]: continue
        nums[j] = False

for _ in range(int(input())):
    s = input().strip()
    solution(s)