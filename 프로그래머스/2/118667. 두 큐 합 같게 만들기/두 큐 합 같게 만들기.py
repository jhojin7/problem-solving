def solution(q1,q2):
    q = q1+q2+q1+q2
    S = sum(q1)+sum(q2)
    i,j = 0,len(q1)-1
    s = sum(q1)
    #print(q[i:j],s,S)
    cnt = 0
    while i<j and j<len(q)-1 and s!=S//2:
        #print(cnt,q[i:j],sum(q[i:j]))
        if s>S//2:
            cnt+=1
            s = s-q[i]
            i+=1
        elif s<S//2:
            cnt+=1
            j+=1
            s+=q[j]
    # print(cnt,s)
    # print(q[i:j],sum(q[i:j]))
    if s==S//2:
        return cnt
    else:
        return -1