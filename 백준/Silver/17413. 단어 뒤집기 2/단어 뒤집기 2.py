import collections

S = collections.deque(list(input().strip()))
word = collections.deque()
tag = []
ans = []
while S:
    c = S.popleft()

    if c=='<':
        ans.append(''.join(word)[::-1])
        word = []
        # S.popleft()
        while S and S[0]!='>':
            tag.append(S.popleft())
        S.popleft()
        ans.append('<')
        ans.append(''.join(tag))
        ans.append('>')
        tag = []
        continue
    
    if c==' ':
        ans.append(''.join(word)[::-1])
        word = []
        ans.append(' ')
        continue

    word.append(c)
# if ans[-1]!=''.join(word)[::-1]:
# print(word)
if word!=[]:
    ans.append(''.join(word)[::-1])
print(''.join(ans))