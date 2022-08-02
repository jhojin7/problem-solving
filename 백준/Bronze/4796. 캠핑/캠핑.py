i =1
while 1:
    l,p,v = map(int,input().split())
    if (l,p,v)==(0,0,0): break
    # l p-l l p-1...
    n = 0
    cnt =0
    while v>0:
        if v-l<0:cnt+=l+(v-l)
        else:cnt+=l
        v-=l
        if not v>0: break
        ###################
        v-=p-l
    print(f"Case {i}: {cnt}")
    i+=1