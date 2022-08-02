for _ in range(int(input())):
    n,s=input().split()
    for c in s:
        for i in range(int(n)): print(c,end='')
    print()