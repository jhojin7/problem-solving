def solution(number):
    ans = 0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                s = number[i]+number[j]+number[k]
                if s==0:
                    ans+=1
    return ans
                
