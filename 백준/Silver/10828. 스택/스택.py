N = int(input())
stack =[]
for _ in range(N):
    cmd, *args = input().split()
    if cmd == "push":
        stack.append(*args)
    elif cmd == "pop":
        if not stack: 
            print(-1)
            continue
        x = stack.pop()
        print(x)
    elif cmd=="size":
        print(len(stack))
    elif cmd=="empty" and not stack:
        print(1)
    elif cmd=="empty" and stack:
        print(0)
    elif cmd=="top":
        if not stack: 
            print(-1)
        else:
            print(stack[-1])
