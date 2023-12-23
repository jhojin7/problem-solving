import collections
N = int(input())
s1 = input().strip()
s2 = input().strip()
c1 = collections.Counter(s1)
c2 = collections.Counter(s2)
if (
    c1 != c2
    or s1[0] != s2[0]
    or s1[-1] != s2[-1]
):
    print("NO")
    exit()

s1 = "".join([c for c in s1 if c not in "aeiou"])
s2 = "".join([c for c in s2 if c not in "aeiou"])
if s1 == s2:
    print("YES")
else:
    print("NO")
