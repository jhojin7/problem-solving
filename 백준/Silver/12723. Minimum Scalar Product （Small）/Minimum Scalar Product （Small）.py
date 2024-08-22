import itertools
for _ in range(int(input())):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    v1perms = itertools.permutations(v1, len(v1))
    v2perms = itertools.permutations(v2, len(v2))
    ans = 999999999999
    for v1perm in v1perms:
        for v2perm in v2perms:
            tmp = 0
            for x,y in zip(v1perm,v2perm):
                tmp+=x*y
            ans = min(ans, tmp)
    print(f"Case #{_+1}: {ans}")
