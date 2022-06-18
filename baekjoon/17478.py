"""
id: 17478
title:재귀함수가뭔가요?
ac: 
"""

str1 = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
str2 = '"재귀함수가 뭔가요?"'
str3 = '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'''
str3_1 = '''마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'''
str3_2 = '''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''
str4 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
str5 = '라고 답변하였지.'

INDENT = "____"
def chatbot(n): 
    print(INDENT*n+ str2)
    if n < N:
        print(INDENT*n + str3)
        print(INDENT*n +str3_1)
        print(INDENT*n+str3_2)
        chatbot(n+1)
    else:
        print(INDENT*n+str4)
    print(INDENT*n+ str5)

N = int(input())
print(str1)
chatbot(0)