def solution(arr):
    stack = [arr.pop(0)]
    for a in arr:
        if stack[-1] != a:
            stack.append(a)
    return stack
        
