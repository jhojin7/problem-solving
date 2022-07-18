import sys,collections
input = sys.stdin.readline
k = int(input())
queue = collections.deque()
for _ in range(k):
    x = int(input())
    if x==0: queue.pop()
    else: queue.append(x)
sys.stdout.write(str(sum(queue)))