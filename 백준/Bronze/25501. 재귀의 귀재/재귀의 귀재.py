import sys

def recursion(s, l, r):
    global cnt
    cnt+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    s = input().strip()
    if isPalindrome(s): sys.stdout.write("1 ")
    else: sys.stdout.write("0 ")
    sys.stdout.write(f"{cnt}\n")