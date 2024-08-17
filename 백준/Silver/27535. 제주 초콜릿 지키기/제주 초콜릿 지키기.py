total = list(map(int, input().split()))
prev = [sum(total)%10]
for _ in range(int(input())):
    eat = list(map(int, input().split()))
    for i,e in enumerate(eat):
        total[i]-=e

    _7h = f"{sum(total)}7H"
    if prev[-1] not in [0,1]:
        # print("prev", prev)
        tmp = sum(total)
        tmp2 = ""
        while tmp>=prev[-1]:
            # print(tmp, tmp2)
            tmp2+=str(tmp%prev[-1])
            tmp//=prev[-1]
        tmp2+=str(tmp)
        _7h = f"{int(tmp2[::-1])}7H"
    if _7h == "7H": _7h = "07H"
    print(_7h)
    prev.append(sum(total)%10)

    if sum(total)==0:
        print("NULL")
    else: 
        srted = sorted(zip(total, "HTCKG"),key=lambda x:(-x[0],x[1]))
        out_s = (''.join([x[1] for x in srted if x[0]!=0]))
        print(out_s)