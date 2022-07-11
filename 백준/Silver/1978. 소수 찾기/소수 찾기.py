import sys
input = sys.stdin.readline
 
def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

N = int(input())
arr = list(map(int,input().split()))
cnt = 0
for num in arr:
    if num == 1:
        continue
    if is_prime(num):
        cnt+=1
print(cnt)