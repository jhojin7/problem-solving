import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

N = int(input())
M = int(input())
S = collections.deque(inputchars())
# print(S)
stack = collections.deque()
ans =0
n = 0
while S:
    # print(stack,n,ans)
    if not stack:
        stack.append(S.popleft())
        continue
    if n==N:
        ans+=1
        n-=1
        # stack = []
        stack.popleft()
        stack.popleft()
        continue
    if stack[0]=='O':
        stack = collections.deque()
        continue

    x = S.popleft()
    if stack[-1]=='I' and x=='O':
        stack.append(x)
    elif stack[-1]=='O' and x=='I':
        stack.append(x)
        n+=1
    elif stack[-1]=='I' and x=='I':
        stack = collections.deque(['I'])
        n = 0
    elif stack[-1]=='O' and x=='O':
        stack = collections.deque()
        n = 0
    # if x=='I' and stack[-1]=='O':
if n==N:
    ans+=1
    n-=1
    # # stack = []
    # stack.popleft()
    # stack.popleft()
# print(ans,stack)
print(ans)