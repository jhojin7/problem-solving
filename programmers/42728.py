def solution(array, commands):
    answer = []
    # while commands:
    #     [i,j,k] = commands.pop(0)
    for i,j,k in commands:
        arr_cut = sorted(array[i-1:j])
        answer.append(arr_cut[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
print(solution(array, commands))