points = {
    'R':0, 'T':0,
    'C':0, 'F':0,
    'J':0, 'M':0,
    'A':0, 'N':0,
}

def solution(survey, choices):
    for surv,choi in zip(survey,choices):
        if choi==1: points[surv[0]]+=3
        elif choi==2: points[surv[0]]+=2
        elif choi==3: points[surv[0]]+=1
        elif choi==5: points[surv[1]]+=1
        elif choi==6: points[surv[1]]+=2
        elif choi==7: points[surv[1]]+=3
    print(points)
    ans = ""
    if points['R'] >= points['T']: ans+='R'
    else: ans+='T'
    if points['C'] >= points['F']: ans+='C'
    else: ans+='F'
    if points['J'] >= points['M']: ans+='J'
    else: ans+='M'
    if points['A'] >= points['N']: ans+='A'
    else: ans+='N'
    print(ans)
    return ans
