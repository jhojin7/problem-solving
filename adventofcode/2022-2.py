arr = []
while 1:
    try: arr.append(''.join(input().split()))
    except: break
score =0
for ab in arr:
    #1 2 3, 0 3 6
    if ab=="AX":   score=score+1+3
    elif ab=="AY": score=score+2+6
    elif ab=="AZ": score=score+3+0

    elif ab=="BX": score=score+1+0
    elif ab=="BY": score=score+2+3
    elif ab=="BZ": score=score+3+6

    elif ab=="CX": score=score+1+6
    elif ab=="CY": score=score+2+0
    elif ab=="CZ": score=score+3+3
print(score)
