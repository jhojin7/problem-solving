"""
id: 9375
title:패션왕신해빈
ac:https://www.acmicpc.net/source/44691826
"""
import itertools
import sys
from io import StringIO
sys.stdin = StringIO("""
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
""".strip())

T = int(input())
for _ in range(T):
    n = int(input())
    type_dict = {}
    for _ in range(n):
        thing, type = input().split()
        if type not in type_dict:
            type_dict[type] = 0
        type_dict[type] += 1
    # print(type_dict)
    # calc ans
    ans = 1
    for x in type_dict.values():
        ans *= (x+1)
    print(ans-1)




    

