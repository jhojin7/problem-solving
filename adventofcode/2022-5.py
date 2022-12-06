stacks = [[] for _ in range(10)]
stacks[1] = list("TDWZVP".strip())
stacks[2] = list("LSWVFJD".strip())
stacks[3] = list("ZMLSVTBH".strip())
stacks[4] = list("RSJ".strip())
stacks[5] = list("CZBGFMLW".strip())
stacks[6] = list("QWVHZRGB".strip())
stacks[7] = list("VJPCBDN".strip())
stacks[8] = list("PTBQ".strip())
stacks[9] = list("HGZRC".strip())

import sys
lines = sys.stdin.readlines()
arr = []
# for l in lines:
#     _,move,_,fr,_,to = l.split()
#     move,fr,to = map(int,[move,fr,to])
#     for _ in range(move):
#         stacks[to].append(stacks[fr].pop())
# for s in stacks[1:]:
#     print(s[-1])

for l in lines:
    _,move,_,fr,_,to = l.split()
    move,fr,to = map(int,[move,fr,to])
    tmp = []
    for _ in range(move):
        tmp.append(stacks[fr].pop())
    stacks[to].extend(tmp[::-1])
# print(stacks)
for s in stacks[1:]:
    print(s[-1],end='')