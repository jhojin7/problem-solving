def solution(players, m, k):
    servercnt = 0
    incrcnt = 0
    servers = [0 for _ in range(25)]
    for i in range(len(players)):
        if i>24: break
        playermax = servers[i]*m
        if players[i]> playermax:
            toincr= (players[i]//m)-servers[i] ###### -servers[i]!!!
            incrcnt+=toincr
            for j in range(i,i+k):
                if j>24: break
                servers[j]+=toincr
    return incrcnt
                
            