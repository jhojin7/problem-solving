import collections
from itertools import count
# s = "bcabc"
s = "cbacdcbc"

# ret = []
# print(s)
# for ch in s:
#     print(ch)
#     if ch not in ret:
#         ret.append(ch)
#         print(ret)
# ret.sort()
# print(''.join(ret))


# ret = []
# print(s)
# counter = collections.Counter(s)
# stack = []
# print(counter)
# for ch in s:
#     # visit ch
#     counter[ch] -= 1
#     # if ch exist in stack, continue
#     if ch in stack:
#         continue
#     while stack and stack[-1] > ch and counter[stack[-1]]>=1:
#         stack.pop()
#     stack.append(ch)
#     print(stack, counter)
# print(stack)


def removeDuplicateLetters_recursion(s:str)->str:
    for first in sorted(set(s)):
        visit = s[s.index(first):]
        print(set(s),set(visit))
        if set(s) == set(visit):
            return first+removeDuplicateLetters_recursion(visit.replace(first,''))
    return ''



ret = removeDuplicateLetters_recursion(s)
print(ret)
