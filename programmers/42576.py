# def solution(participant, completion):
#     chars = "abcdefghijklmnopqrstuvwxyz"
#     all = {}
#     for c in chars: all[c] = []
#     for p in participant:
#         all[p[0]].append(p)
#     for comp in completion:
#         all[comp[0]].remove(comp)
#     ret = []
#     for x in all.values():
#         ret += x
#     return ret[0]


# def solution(participant, completion):
#     participant = sorted(participant)
#     completion = sorted(completion)
#     #print(participant, completion)
    
#     for person in participant:
#         if person not in completion:
#             return person
#         else: completion.remove(person)


def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for c in range(len(completion)):
        if completion[c] != participant[c]:
            return participant[c]
    return participant[c+1]