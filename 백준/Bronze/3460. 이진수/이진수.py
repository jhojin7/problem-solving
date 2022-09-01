for _ in range(int(input())):
    n=int(input())
    i=0
    while n:
        if n%2==1: print(i,end=' ')
        i+=1
        n//=2
    print()