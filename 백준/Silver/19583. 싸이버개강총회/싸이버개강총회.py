S, E, Q = input().split()
sh, sm = map(int, S.split(":"))
S = sm+sh*60
eh, em = map(int, E.split(":"))
E = em+eh*60
qh, qm = map(int, Q.split(":"))
Q = qm+qh*60
start, end = set(), set()
while 1:
    try:
        hhmm, name = input().split()
    except:
        break
    h, m = map(int, hhmm.split(':'))
    T = m+h*60
    if T <= S:
        start.add(name)
    elif E <= T <= Q:
        end.add(name)

print(len(start.intersection(end)))
