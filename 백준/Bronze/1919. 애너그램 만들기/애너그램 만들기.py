import sys,collections
input = sys.stdin.readline
str1 = collections.Counter(input().strip())
str2 = collections.Counter(input().strip())
all_keys = set(list(str1.keys())+list(str2.keys()))
# print(all_keys)
ans = 0
for key in all_keys:
    c1,c2 = str1[key],str2[key]
    # print(c1,c2)
    if c1==c2: continue
    diff = abs(c1-c2)
    ans += diff
print(ans)