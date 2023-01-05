def solution(sizes):
    xx,yy = [],[]
    for x,y in sizes:
        xx.append(min(x,y))
        yy.append(max(x,y))
    return max(xx)*max(yy)
