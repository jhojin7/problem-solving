# 없는숫자더하기
def solution(numbers):
    return sum([1,2,3,4,5,6,7,8,9,0]) - sum(numbers)
input = [1,2,3,4,6,7,8,0]
# input = [5,8,4,0,6,7,9]
print(solution(input))