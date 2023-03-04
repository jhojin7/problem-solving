import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()


N= int(input())
pattern = input().rstrip().split('*')
front,rear = pattern[0],pattern[1]
# print(front,rear)
def solve():
    global front,rear
    name = collections.deque(input().strip())
    fr,rer = [],[]
    while name and len(fr)<len(front):
        fr.append(name.popleft())
    while name and len(rer)<len(rear):
        rer.append(name.pop())
    rer=reversed(rer)

    # fr = name[:len(front)]
    # rer = name[-len(rear):]
    fr,rer = ''.join(fr),''.join(rer)
    # print(front,rear)
    # print(fr,rer)
    if fr==front and rer==rear:
        print("DA")
    else: print("NE")
for _ in range(N):
    solve()