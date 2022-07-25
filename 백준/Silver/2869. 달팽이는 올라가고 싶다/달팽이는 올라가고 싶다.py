import sys, math
input = sys.stdin.readline
A,B,V = map(int,input().split())
# tot_dist = A*days-B*days+A #+A for next day's A
# A*days-B*days+A >= V
# days >= (V-A)/(A-B)
sys.stdout.write(str(math.ceil((V-A)/(A-B)+1)))