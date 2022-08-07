import sys
input = sys.stdin.readline
output = sys.stdout.write

def half_adder(a,b,carry):
    _carry = 0
    s = int(a)+int(b)+carry
    if s>=10:
        _carry = s//10
        s = s%10
    return (_carry,s)

def full_adder(A,B):
    carry = 0
    ans = ""
    ia,ib = len(A)-1,len(B)-1
    while ia>=0 and ib>=0:
        carry,s = half_adder(A[ia],B[ib],carry)
        # print(A[ia],B[ib],carry,s)
        ans = str(s) + ans
        # print(ans)
        ia-=1
        ib-=1

    while ia>=0:
        carry,s = half_adder(A[ia],'0',carry)
        ans = str(s) + ans
        ia-=1

    while ib>=0:
        carry,s = half_adder('0',B[ib],carry)
        ans = str(s) + ans
        ib-=1

    # print(ia,ib,s,carry)
    if carry!=0: return str(carry)+ans
    else: return ans

A,B=input().split()
output(str(full_adder(A,B)))