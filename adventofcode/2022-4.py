import sys
arr = sys.stdin.readlines()
arr = [a.strip().split(',') for a in arr]
cnt =0
for a,b in arr:
    aa = list(map(int,a.split('-')))
    bb = list(map(int,b.split('-')))
    if (aa[0]<=bb[0] and bb[1]<=aa[1]
        or bb[0]<=aa[0] and aa[1]<=bb[1]
        or aa[1]<=bb[0] or bb[1]<=aa[0]):
        cnt+=1
print(cnt)

