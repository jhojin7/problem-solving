import sys, collections, heapq, math, re, random
input=sys.stdin.readline

S=list(input().strip())
T=list(input().strip())

while T:
    # print(T)
    if T==S:
        print(1)
        exit()
    if T[-1]=='A':
        T.pop()
        if T==S:
            print(1)
            exit()

    elif T[-1]=='B':
        T.pop()
        T.reverse()
        if T==S:
            print(1)
            exit()
print(0)