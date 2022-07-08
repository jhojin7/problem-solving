import sys,math
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
Ts = list(map(int,input().split()))
# print(N,Ts)
cnt,ans = 3,0
to_find = Ts[:N-2]
# print(to_find, math.prod(to_find))
# lcm
lcm = 1
for x in to_find:
    lcm = lcm*x//math.gcd(lcm,x)
output(str(lcm))