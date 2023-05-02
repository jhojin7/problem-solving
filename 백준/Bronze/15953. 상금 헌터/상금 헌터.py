for _ in range(int(input())):
    a,b = map(int,input().split())
    ans = 0
    if a==1: ans+=500
    elif 1<a<=3: ans+=300
    elif 3<a<=6: ans+=200
    elif 6<a<=10: ans+=50
    elif 10<a<=15: ans+=30
    elif 15<a<=21: ans+=10
    else: ans+=0

    if b==1: ans+=512
    elif 1<b<=3: ans+=256
    elif 3<b<=7: ans+=128
    elif 7<b<=15: ans+=64
    elif 15<b<=15+16: ans+=32
    else: ans+=0
    print(ans*10000)