def solution(s):
    def check(ss:list):
        mapper = {'{':'}','[':']','(':')'}
        q = []
        for i in range(len(ss)):
            if ss[i] in "({[":
                q.append(ss[i])
            else:
                if len(q)>0 and q[-1] in mapper.keys() and mapper[q[-1]]==ss[i]:
                    q.pop()
                else:
                    q.append(ss[i])
        if q:
            return False
        return True
    
    arr = list(s.strip())
    ans = 0
    for _ in range(len(s)):
        #print(arr,check(arr))
        if check(arr):
            ans+=1
        arr.append(arr.pop(0))
    return ans