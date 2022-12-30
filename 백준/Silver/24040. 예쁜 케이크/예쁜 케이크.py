T=int(input())
for _ in range(T):
    N=int(input())
    # print(1,N//1)
    # print(2,N/2)
    # print(3,N/3)
    if N%2==0:
        cnt = 2*2+(N//2)*2
        if cnt%3==0:
            print("TAK")
            continue
    if N%3==0:
        cnt = 3*2+(N//3)*2
        if cnt%3==0:
            print("TAK")
            continue
    cnt = 1*2+(N)*2
    if cnt%3==0:
        print("TAK")
    else:
        print("NIE")