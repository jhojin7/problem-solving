import sys,collections
input = sys.stdin.readline
k = int(input())
stack = collections.deque()
for _ in range(k):
    x = int(input())
    if x==0: stack.pop()
    else: stack.append(x)
sys.stdout.write(str(sum(stack)))