for _ in range(int(input())):
    N=int(input())
    rus=list(map(int,input().split()))
    kor=list(map(int,input().split()))
    kor.sort()
    vis=set()
    for i in range(N):
        for j in range(N):
            if j not in vis and rus[i]<=kor[j]:
                vis.add(j)
                break
        # print(vis)
    print(len(vis))