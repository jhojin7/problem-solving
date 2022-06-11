import sys, io
tc = """
16 4
noj.am IU
acmicpc.net UAENA
startlink.io THEKINGOD
google.com ZEZE
nate.com VOICEMAIL
naver.com REDQUEEN
daum.net MODERNTIMES
utube.com BLACKOUT
zum.com LASTFANTASY
dreamwiz.com RAINDROP
hanyang.ac.kr SOMEDAY
dhlottery.co.kr BOO
duksoo.hs.kr HAVANA
hanyang-u.ms.kr OBLIVIATE
yd.es.kr LOVEATTACK
mcc.hanyang.ac.kr ADREAMER
startlink.io
acmicpc.net
noj.am
mcc.hanyang.ac.kr
"""
sys.stdin = io.StringIO(tc.strip())

import collections
N, M = map(int,input().split()) 
# passwords[site] = pw
passwords = collections.defaultdict()
# input
for _ in range(N):
    site, pw = map(str,input().split()) 
    passwords[site] = pw
# search
for _ in range(M):
    _site = str(input())
    print(passwords[_site])