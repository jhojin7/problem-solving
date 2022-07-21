import sys
input = sys.stdin.readline
# print = sys.stdout.write
nums = []
N,*nums = input().split()
N = int(N)-len(nums)
# print(N,nums)
while N>0:
    row = input().split()
    nums.extend(row)
    N -= len(row)
ints = []
for x in nums:
    nx = int(x[::-1])
    ints.append(nx)
print(*sorted(ints),sep='\n')