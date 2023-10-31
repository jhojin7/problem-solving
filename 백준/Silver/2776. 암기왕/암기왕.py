for _ in range(int(input())):
    N = int(input())
    arr = set(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))
    for x in arr2:
        if x in arr:
            print(1)
        else:
            print(0)
