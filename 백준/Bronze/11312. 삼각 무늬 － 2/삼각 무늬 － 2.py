for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==b: 
        print(1)
        continue
    c = a//b
    print(c*c)