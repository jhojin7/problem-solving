import collections
S = collections.deque(input().strip())
N = len(S)
stack = []
stack.append(S.popleft())
while stack:
    if not S:
        break
    c = S.popleft()
    if c == 'P':
        stack.append(c)
        continue
    # if c=='A'
    if len(stack) < 2:
        stack.append(c)
        continue
    if not S:
        stack.append(c)
        continue

    if ((len(stack) >= 2 and stack[-2] == 'P' and stack[-1] == 'P')
            and (S and S[0] == 'P')):
        stack.pop()
        stack.pop()
        S.popleft()
        stack.append('P')
    else:
        break
if ''.join(stack) not in ["P", "PPAP"]:
    print("NP")
else:
    print("PPAP")
