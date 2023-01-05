def solution(answers):
    aa,bb,cc=0,0,0
    for i in range(len(answers)):
        a = [1,2,3,4,5][i%5]
        b = [2,1,2,3,2,4,2,5][i%8]
        c = [3,3,1,1,2,2,4,4,5,5][i%10]
        if answers[i]==a: aa+=1
        if answers[i]==b: bb+=1
        if answers[i]==c: cc+=1
    print(aa,bb,cc)
    ret = []
    if max(aa,bb,cc)==aa: ret.append(1)
    if max(aa,bb,cc)==bb: ret.append(2)
    if max(aa,bb,cc)==cc: ret.append(3)
    print(sorted(ret))
    return sorted(ret)