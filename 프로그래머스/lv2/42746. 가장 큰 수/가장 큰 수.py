import functools
def comp(n1,n2):
    if n1+n2<n2+n1: 
        return 1
    elif n1+n2>n2+n1: 
        return -1
    else:
        return 0

def solution(numbers):
    nums = list(map(str,numbers))
    nums.sort(key=functools.cmp_to_key(comp))
    if nums[0]=="0": return '0'
    return ''.join(map(str,nums))