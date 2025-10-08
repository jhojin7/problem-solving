import collections
def solution(record):
    resp = []
    d = collections.defaultdict(str)
    state = collections.defaultdict(str)
    
    for r in record:
        action, *uid_uname = r.split(' ')
        #print(r, action, uid_uname)
        if action=='Leave':
            uid = uid_uname[0]
            continue
        uid,uname= uid_uname[0], uid_uname[1]
        if action=='Enter':
            d[uid] = uname
        elif action=='Change':
            d[uid] = uname
    for r in record:
        action, *uid_uname = r.split(' ')
        if action=='Enter':
            resp.append(f"{d[uid_uname[0]]}님이 들어왔습니다.")
        elif action=='Leave':
            resp.append(f"{d[uid_uname[0]]}님이 나갔습니다.")
    #print(resp)
    #print(d)
    return resp