"""
https://programmers.co.kr/learn/courses/30/lessons/42747
0/100
"""
def solution(citations):
    cits = sorted(citations)
    h = len(cits)//2
    while 0<h and h<len(cits):
        # print(h,cits[:h], cits[h:])
        if cits[h-1] > h: h -= 1
        elif h > cits[h]: h += 1
        # if cits[h-1] < h and h <= cits[h]\
        else:# len(cits[:h]) < h and h <= len(cits[h:]):
            return h+1
    return h

print(solution([1,1,1,1,1,1]))
print(solution([3,0,6,1,5]))
print(solution([3,0,4,2,6,1,7]))
print(solution([1,2,3,4,5,6,7,8]))