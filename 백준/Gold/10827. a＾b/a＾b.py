import sys, collections, itertools, heapq, math, re, random
input=sys.stdin.readline
def inputint():return map(int,input().split())
def inputchars():return input().strip()

import decimal
decimal.getcontext().prec = 1000000
a,b = input().split()
a = decimal.Decimal(a)
b = int(b)
# c = decimal.Decimal(1.0)
c = a**b
# print(a,b,c)
# for _ in range(b):
#     c*=a
print(f"{c:.100000f}".rstrip('0'))
# print(c)
# print(str(c.normalize()).rstrip('0'))
# print(str(c*10))

# d = decimal.Decimal('0.0000000001')
# result = d.quantize(decimal.Decimal('0.0000000001'), rounding=decimal.ROUND_DOWN)
# print(result)

# print(decimal.Decimal(0.0000000001).quantize())
# print(decimal.Decimal(0.01).normalize())