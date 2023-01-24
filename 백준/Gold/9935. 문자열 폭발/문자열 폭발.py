import collections
s=collections.deque(input().strip())
bomb=input()
stack=collections.deque([])

while s:
    # if not stack:
    #     stack.append(s.popleft())
    stack.append(s.popleft())
    if len(stack)>=len(bomb) and stack[-1]==bomb[-1]:
        ok=True
        for i in range(len(bomb)):
            if stack[-1-i]!=bomb[-1-i]:
                ok=False
        if ok:
            for _ in range(len(bomb)):
                stack.pop()
if not stack: print("FRULA")
else: print(''.join(stack))
