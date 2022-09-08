for _ in range(int(input())):
    # 25 10 5 1
    c=int(input())
    x=c//25
    c%=25
    y=c//10
    c%=10
    z=c//5
    c%=5
    w=c
    print(x,y,z,w)