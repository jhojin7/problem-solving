h=int(input())
#0469 8
if h==0: print(1)
elif h==1: print(0)
elif h%2==0:
    ans = ['8' for _ in range(h//2)]
    print("".join(ans))
else:
    ans = ['4']+['8' for _ in range(h//2)]
    print("".join(ans))