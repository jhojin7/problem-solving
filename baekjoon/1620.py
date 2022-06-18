"""
id: 1620
title:나는야 포켓몬 마스터 이다솜
ac: https://www.acmicpc.net/source/44692360
"""

import sys
N, M = map(int,sys.stdin.readline().split())
pokemon = {}
pokemon2 = {}

for i in range(N):
    name = sys.stdin.readline().strip()
    pokemon[i+1] = name
    pokemon2[name] = i+1
# print(pokemon, pokemon2)

for _ in range(M):
    question = sys.stdin.readline().strip()
    if question.isnumeric():
        print(pokemon[int(question)])
    else:
        print(pokemon2[question])