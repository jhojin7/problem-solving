import collections
s = input().strip()
evals = collections.defaultdict(int)

def op(left,right,op):
    return eval(str(left)+op+str(right))

def recurse(s):
    # base case
    if s.isdigit():
        evals[s] = int(s)
        return int(s)
    # dp
    if s in evals.keys():
        return evals[s]
    # recurse
    choices = []
    for i in range(len(s)):
        if s[i] in "+-":
            left = recurse(s[:i])
            right = recurse(s[i+1:])
            choices.append(op(left,right,s[i]))
    evals[s] = min(choices)
    return evals[s]

ans = recurse(s)
print(ans)