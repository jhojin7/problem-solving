def solution(today, terms, privacies):
    ans = []
    term = dict()
    terms = [t.split() for t in terms]
    for t,mm in terms:
        term[t] = int(mm)
    privacies = [p.split() for p in privacies]
    def parse(yyyymmdd):
        yyyy,mm,dd = list(map(int,yyyymmdd.split('.')))
        return yyyy*28*12+mm*28+dd
    for idx, priv in enumerate(privacies):
        yyyymmdd, c = priv
        diff = parse(yyyymmdd)+term[c]*28-1 - parse(today)
        if diff<0:
            ans.append(idx+1)
    print(ans)
    return ans
            
        