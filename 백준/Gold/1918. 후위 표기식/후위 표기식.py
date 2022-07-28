import sys
input = sys.stdin.readline

infix = input().strip()
# print(infix)
postfix = []
stack = []

idx = 0
while idx<len(infix):
    cur = infix[idx]
    if cur=='(':
        stack.append(cur)
    elif cur==')':
        while stack and stack[-1]!='(':
            postfix.append(stack.pop())
        stack.pop()
    elif cur in "*/":
        while stack and stack[-1] in "*/":
            postfix.append(stack.pop())
        stack.append(cur)
    elif cur in "+-":
        while stack and stack[-1]!="(": # 후순위
            postfix.append(stack.pop())
        stack.append(cur)
    else:
        postfix.append(cur)

    # print(postfix,stack)
    idx+=1

while len(stack)>0:
    postfix.append(stack.pop())
print(''.join(postfix))