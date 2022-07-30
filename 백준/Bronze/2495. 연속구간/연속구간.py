a = list(input().strip())
b = list(input().strip())
c = list(input().strip())
def testcase(s):
    i = 0
    maxcnt = -9999999
    while i<len(s):
        cnt = 1
        while i+1<len(s) and s[i]==s[i+1]:
            i+=1
            cnt+=1
        maxcnt = max(cnt,maxcnt)
        i+=1
    return maxcnt
print(testcase(a))
print(testcase(b))
print(testcase(c))