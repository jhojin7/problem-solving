import sys
input = sys.stdin.readline

def testcase():
    score = []
    s = list(input().strip())
    # print(s)
    cnt = 0
    prev = s.pop()

    if prev=='O':
        if s and prev=='O' and s[-1]=='O': 
            score.append(1)
            cnt+=1
        else:
            score.append(1)
            cnt+=1

    while s:
        cur = s.pop()
        if cur=='O':
        # if s and s[-1]==cur:
            cnt+=1
            score.append(cnt)
        else:
            cnt = 0
            score.append(cnt)
        prev = cur
    # print(score)
    return sum(score)

t = int(input())
for _ in range(t):
    print(testcase())