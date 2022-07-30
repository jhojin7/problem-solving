def testcase():
    N = int(input())
    parent = [0 for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        parent[b] = a

    find1,find2 = map(int,input().split())
    path1,path2 = [],[]

    cur = find1
    path1.append(cur)
    while parent[cur]!=0: 
        path1.append(parent[cur])
        cur = parent[cur]

    cur = find2
    path2.append(cur)
    while parent[cur]!=0: 
        path2.append(parent[cur])
        cur = parent[cur]

    for i in range(len(path1)):
        for j in range(len(path2)):
            if path1[i]==path2[j]:
                return path1[i]

T = int(input())
for _ in range(T):
    print(testcase())