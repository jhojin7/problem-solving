def check1(n):
    if n == q[0]: return True
    else: return False

def check2(n):
    found = 1
    for i in range(1,len(q)-1):
        if q[i] == n:
            return found
        found +=1
    return found

def check3(n):
    found = 1
    for i in range(len(q)-1,-1,-1):
        if q[i] == n:
            return found
        found +=1
    return found

import sys,collections
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
find = list(map(int,input().split()))
q = collections.deque(arr)
# find = collections.deque(find)
# print(q,find)

ans = 0
for idx in range(M):
    ch1,ch2,ch3 = (check1(find[idx]),check2(find[idx]),check3(find[idx]))
    # print(find[idx],q)
    # print(ch1,ch2,ch3)

    if ch1:
        q.popleft()
    elif ch2 <= ch3:
        ans+=ch2
        while ch2!=0:
            q.append(q.popleft())
            ch2-=1
        q.popleft()
    elif ch2 > ch3:
        ans+=ch3
        while ch3!=0:
            q.appendleft(q.pop())
            ch3-=1
        q.popleft()
#     print("ans",ans)
# print(q)
print(ans)