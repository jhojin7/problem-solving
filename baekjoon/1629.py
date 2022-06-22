"""
id: 1629
title:곱셈
ac:https://www.acmicpc.net/source/44868833
https://medium.datadriveninvestor.com/fast-exponentiation-using-dynamic-programming-48e36285e320
https://docs.python.org/3/library/functions.html#pow
https://en.wikipedia.org/wiki/Modular_exponentiation
"""
import sys
from io import StringIO
from timeit import timeit
sys.stdin = StringIO("""
1 1 1
""".strip())
# 2147483646 2147483646 2147483647
# 1 2 3
# 10 11 12
# 1 1 1!!!!!!!!!!!!!!!!!!!!1

# (A**B)%C
A, B, C = map(int, sys.stdin.readline().split())
print(A, B, C)

def exp(a, b):
    # stop recursion
    if b == 1:
        return a % C
    elif b == 0:
        return 1

    # check if B is even or odd
    tmp = exp(a, b//2) # recursion
    if b % 2 == 1:
        return (a * tmp * tmp) % C
    else:
        # tmp = exp(a, b//2)
        return (tmp * tmp) % C

py = timeit("print(pow(A,B,C))", globals=globals(), number=1)
print(py,pow(A,B,C))

t = timeit("print(exp(A,B))", globals=globals(), number=1)
print(t)