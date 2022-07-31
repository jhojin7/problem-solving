while 1:
    n = float(input())
    if n==0: break
    s = 1
    s += n
    s += n*n
    s += n*n*n
    s += n*n*n*n
    print("{:.2f}".format(s))