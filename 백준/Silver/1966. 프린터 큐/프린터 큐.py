import collections
for _ in range(int(input())):
    N,M = list(map(int,input().split()))
    q = collections.deque(map(int,input().split()))
    docs = collections.deque(range(1,N+1))
    # print(docs)
    # print(N,M,q)
    cnt = 0
    find = docs[M]
    while q:
        if max(q) == q[0]:
            q.popleft()
            out = docs.popleft()
            cnt+=1
            if out==find: print(cnt)
        else:
            q.append(q.popleft())
            docs.append(docs.popleft())
    #     print(docs)
    # print()