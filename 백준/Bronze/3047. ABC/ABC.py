import sys
input = sys.stdin.readline

nums = list(map(int,input().split()))
abc = input().strip()
nums.sort()
for x in abc:
    if x=='A': sys.stdout.write(f"{nums[0]} ")
    elif x=='B': sys.stdout.write(f"{nums[1]} ")
    elif x=='C': sys.stdout.write(f"{nums[2]} ")