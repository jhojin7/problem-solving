def deci2n(deci, n)->str:
    ret = ''
    hexstr="0123456789ABCDEF"
    while deci >= n:
        ret=hexstr[deci%n]+ret
        deci//=n
    ret=hexstr[deci]+ret
    return ret

def solution(n, t, m, p):
    arr = []
    print(deci2n(8,7))
    for x in range(0,100001):
        arr.extend(deci2n(x, n).strip())
    tube = [arr[i] for i in range(p-1,len(arr),m)]
    tu = ''.join(tube)
    return tu[:t]
        
        
        
        
        
