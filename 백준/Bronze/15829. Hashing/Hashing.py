import sys
input = sys.stdin.readline
int(input())
r = 31
M = 1234567891

def alpha(ch):
    for i,x in enumerate("abcdefghijklmnopqrstuvwxyz"):
        if x==ch:
            return i+1

def H(str):
    ans = 0
    for i,ch in enumerate(str):
        # print(i,ch,alpha(ch))
        tmp = alpha(ch)*(pow(r,i,M))
        ans += tmp%M
    return ans%M

str = input().strip()
print(H(str)%M)