import sys, collections
input = sys.stdin.readline

N = int(input())
stack = collections.deque()
for _ in range(N):
    query = input().split()
    if query[0] == "push":
        stack.append(query[1])
    elif query[0] == "pop":
        try: print(stack.pop())
        except: print(-1)
    elif query[0] == "size":
        print(len(stack))
    elif query[0] == "empty":
        if len(stack) == 0: print(1)
        else: print(0)
    elif query[0] == "top":
        if len(stack) != 0:
            print(stack[-1])
        else: print(-1)