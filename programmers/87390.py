def solution(n,left, right):
    # time limit...
    # make 2d matrix
    # mat = [[0 for j in range(n)] for i in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         if i<=j: mat[i][j] = j+1
    #         else: mat[i][j] = i+1
    # calculate answer
    # for i in range(len(mat)):
    #     answer += mat[i]
    # return (answer[left:right+1])

    # # time limit AC
    # answer = []
    # for i in range(left//n-1,right//n+1):
    #     for j in range(n):
    #         ansIdx = i*n+j 
    #         if ansIdx >= left and ansIdx <= right:
    #             if i<=j: answer.append(j+1)
    #             else: answer.append(i+1)
    # return answer

    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
    return answer

ans = solution(3,2,5)# n*i+j
# ans = solution(4,7,14)# n*i+j
# ans = solution(10000,7,14)# n*i+j
print(ans)