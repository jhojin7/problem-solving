# def solution(id_list, report, k):
#     print(id_list, report, k)
#     # init df
#     import pandas
#     df = pandas.DataFrame(id_list,columns=['user'])
# # [id_list,None,None],colums=['user','reports','stopped']

#     # count reports
#     for rep in report:
#         fr, to = rep.split()
#         print(fr,"->",to)
#     print(report_cnt,report_cnt.values())

#     print(df)
#     answer = []
#     return answer



# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k, result = 2, [2,1,1,0]
# # id_list = ["con", "ryan"]
# # report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# # k, result = 3, [0,0]
# ans = solution(id_list, report, k)
# print(ans)