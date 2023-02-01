import itertools, collections
def solution(word):
    alpha="AEIOU"
    words = []
    stack = [(0,"")]
    while stack:
        cur,curword = stack.pop()
        words.append(curword)
        if len(curword)==5: continue
        for i in range(5):
            nxtword = curword + str(alpha[i])
            stack.append((i,nxtword))
    words.sort()
    for i,w in enumerate(words):
        if w==word:
            print(i)
            return i