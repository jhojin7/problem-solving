import collections
def solution(genres, plays):
    d = collections.defaultdict(list)
    labld = collections.defaultdict(list)
    i=0
    for g,p in zip(genres, plays):
        d[g].append(p)
        labld[g].append((p,i))
        i+=1
    #print(d)
    #print(labld)
    
    sums = {}
    for k,v in d.items():
        sums[k]=sum(v)
    sums = (sorted(sums.items(),key=lambda x:-x[1]))
    ans=[]
    for k,_ in sums:
        a = (sorted(labld[k],key=lambda x:(-x[0],x[1])))
        if len(a)>=2:
            ans.append(a[0][1])
            ans.append(a[1][1])
        elif len(a)==1:
            ans.append(a[0][1])
    return ans
    
