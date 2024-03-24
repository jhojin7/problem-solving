import itertools
nums = sorted(itertools.permutations(range(1,10),3))

for _ in range(int(input())):
    cur, strike, ball = map(int,input().split())
    cur = str(cur)
    if strike==3:
        print(1)
        exit()
    _nums = []
    for num in nums:
        _strike, _ball = 0,0
        for i in range(3):
            if str(num[i])==(cur[i]):
                _strike +=1
            elif str(num[i]) in cur:
                _ball +=1
        if strike==_strike and ball==_ball:
            _nums.append(num)
    nums = _nums
print(len(nums))