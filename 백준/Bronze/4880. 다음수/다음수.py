while True:
    a,b,c = map(int,input().split())
    if a==b==c==0: break
    elif b-a == c-b:
        print(f"AP {c+(c-b)}")
    elif b/a == c/b:
        print(f"GP {c*(c//b)}")