import sys,collections
input = sys.stdin.readline
N = int(input())
nums = set(map(int,input().split()))
M = int(input())
query = collections.deque(map(int,input().split()))
while query:
    q = query.popleft()
    if q in nums: sys.stdout.write("1\n")
    else: sys.stdout.write("0\n")