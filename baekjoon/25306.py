"""
id: 25306
title:연속xor
ac:https://www.acmicpc.net/source/45173720
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
3 5
""".strip())
# 10000000000
import sys,operator
A,B = map(int,sys.stdin.readline().split())
# print(A,B,str(bin(A)),int("11",base=2))
# print(format(A,'064b'))

# print(format(10**18,"064b"))
strA = format(A,"064b")
strB = format(B,"064b")

# ans = strA
# n = A+1
# while n <= B:
#     # ans ^= n
#     ans = text_xor(ans,format(n,"064b"))
#     n += 1
# print(ans)
# print(int(ans,2))

# arr = [2,3,4,5,6,7,8,9]
# n = 1
# for a in range(2,20):
#     n ^= a
#     print(a,format(n,"08b"))

A,B = map(int,input().split())
def find(x):
    if x%4 == 0:
        return x
    elif x%4 == 1:
        return 1
    elif x%4 == 2:
        return x+1
    elif x%4 == 3:
        return 0
print(find(A-1)^find(B))
