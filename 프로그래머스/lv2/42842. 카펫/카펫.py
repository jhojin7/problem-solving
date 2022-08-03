def solution(brown, yellow):
    for x in range(5000):
        for y in range(5000):
            if ((x-2)*(y-2)==yellow
                and 2*x+2*(y-2)==brown):
                return [y,x]
