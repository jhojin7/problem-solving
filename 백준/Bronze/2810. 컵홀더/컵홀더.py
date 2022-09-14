N=int(input())
seats=list(input().strip())
for i in range(len(seats)-1):
    if i+1<len(seats) and seats[i]=='L' and seats[i+1]=='L':
        seats[i]="LL"
        seats.pop(i+1)
i=0
while i<len(seats):
    seats.insert(i,0)
    i+=2
seats+=[0]
tot=seats.count(0)

# LL
for i in range(len(seats)):
    if seats[i]=="LL":
        seats[i-1]=1
        seats[i+1]=1
# print(seats)
# S
for i in range(1,len(seats)-1,2):
    prev=seats[i-1]
    next=seats[i+1]
    if seats[i]!="S": continue
    if (prev,next)==(1,1): continue
    elif (prev,next)==(0,1):
        seats[i-1]+=1
        # seats[i+1]+=1
    elif (prev,next)==(1,0):
        seats[i+1]+=1
        # seats[i+1]+=1
    else:
        seats[i-1]+=1
        # seats[i+1]+=1
# print(seats)
print(tot-seats.count(0))