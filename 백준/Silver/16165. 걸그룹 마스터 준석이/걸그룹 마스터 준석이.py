import sys, collections
input = sys.stdin.readline
N, M = map(int,input().split())
groups = collections.defaultdict(list)
for _ in range(N):
    gr_name = input().strip()
    n = int(input())
    for _ in range(n):
        groups[gr_name].append(input().strip())
    groups[gr_name].sort()

for _ in range(M):
    query = input().strip()
    typee = int(input())
    if typee == 0:
        for name in groups[query]:
            print(name)
    elif typee==1:
        for gr_name in groups.keys():
            for name in groups[gr_name]:
                if name == query:
                    print(gr_name)
                    break