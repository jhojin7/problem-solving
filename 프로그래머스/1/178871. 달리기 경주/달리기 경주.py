from copy import deepcopy

def solution(players, callings):
    d = {}
    d2 = {}
    for i,player in enumerate(players):
        d[i] = player
        d2[player] = i
    for call in callings:
        idx = d2[call]
        players[idx-1], players[idx] = \
            players[idx], players[idx-1]
        d2[players[idx-1]], d2[players[idx]] = \
            d2[players[idx]], d2[players[idx-1]]
    return players