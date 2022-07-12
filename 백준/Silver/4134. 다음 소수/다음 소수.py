import sys,math
input = sys.stdin.readline

def is_prime(n):
    if n in [0,1]: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

N = int(input())
for _ in range(N):
    x = int(input())
    for n in range(x,4*10**10):
        if is_prime(n):
            print(n)
            break