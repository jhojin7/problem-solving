import sys, datetime
input = sys.stdin.readline

N = int(input())
if N==0: 
    print(0)
    exit()
times = []
lis = []
for _ in range(N):
    yymmdd,hhmmss,li = input().strip().split()
    year,_,_ = yymmdd.split('/')
    yymmdd = (datetime.date.fromisoformat('-'.join(yymmdd.split('/'))))
    hhmmss = (datetime.time.fromisoformat(hhmmss))
    times.append(datetime.datetime.combine(yymmdd,hhmmss))
    lis.append(int(li))

pis = []
yeardelta = 0
for i in range(N):
    yeardelta = datetime.datetime(int(times[i].year),12,31,23,59,59)-datetime.datetime(int(times[i].year),1,1,0,0,0)
    tnti = (times[N-1]-times[i])

    import calendar
    if calendar.isleap(times[i].year):
        tnti = tnti + datetime.timedelta(seconds=86400)
    p_i = max(
        0.5**(tnti.total_seconds()/yeardelta.total_seconds()),
        0.9**(N-i-1)
    )
    pis.append(p_i)

for i in range(N):
    timediff = times[N-1]-times[i]
    diffdays = timediff.days
    diffhours = (timediff.total_seconds()-timediff.days*86400)//3600
    diffdiff = datetime.timedelta(days=diffdays,hours=diffhours)/yeardelta.total_seconds()

X = sum([pis[i]*lis[i] for i in range(N)])/\
    sum([pis[i] for i in range(N)])
print(round(X))