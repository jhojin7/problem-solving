def solution(s):
    ans = 0
    tmps = []
    
    prev = 0
    for i in range(len(s)):
        if s[i] in "SDT":
            tmps.append(s[prev:i+1])
            prev = i+1
        elif s[i] == "#":
            tmps[-1]+='#'
            prev = i+1
        elif s[i] == "*":
            tmps[-1]+='*'
            if len(tmps)>1:
                tmps[-2]+='*'
            prev = i+1
    for tmp in tmps:
        if "S" in tmp:
            num,*prize = tmp.split("S")
            x = int(num)
            if not prize: continue
            for p in prize[0]:
                if p=='*':x*=2
                if p=='#':x*=-1
        elif "D" in tmp:
            num,*prize = tmp.split("D")
            x = int(num)**2
            if not prize: continue
            for p in prize[0]:
                if p=='*':x*=2
                if p=='#':x*=-1
        elif "T" in tmp:
            num,*prize = tmp.split("T")
            x = int(num)**3
            if not prize: continue
            for p in prize[0]:
                if p=='*':x*=2
                if p=='#':x*=-1
        ans+=x
    return(ans)
            
            
                