def solution(s):
    s = list(s.strip())
    stack = [s.pop(0)]
    for c in s:
        if not stack:
            stack.append(c)
        elif stack[-1]=='(' and c==')':
            stack.pop()
        else:
            stack.append(c)
    print(stack)
    if stack: return False
    else: return True
