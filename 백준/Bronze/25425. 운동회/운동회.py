import math
N,M,a,K = map(int,input().split())
total = N*M
if M==1: 
    print(a,a)
    exit()
# teams remaining
# max 지금 기준 우리팀이 꼴지할경우. 우리팀 나빼고 다죽음. 
# 다른팀 다살아있음. 내가 우리팀 마지막으로 죽을 경우.
mmax = N-1
# min 우리팀 풀피. a명 남은애들 꽉꽉 채워서 팀만들기. 
# print(a-K) # 전체남은사람a - 우리팀남은사람k
# 저 인원 가지고 묶어서 팀을 만들기
mmin = math.ceil((a-K)/M)
print(mmax+1, mmin+1)