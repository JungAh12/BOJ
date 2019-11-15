def solution(record):
    answer = []
    usrNick = {}
    for rec in record:
        if rec.find("Enter") is not -1 or rec.find("Change") is not -1:
            usrNick[rec.split(' ')[1]] = rec.split(' ')[2]

    for rec in record:
        if rec.split(' ')[0] == 'Enter':
            answer.append(usrNick[rec.split()[1]]+'님이 들어왔습니다.')
        elif rec.split(' ')[0] == 'Leave':
            answer.append(usrNick[rec.split()[1]]+'님이 나갔습니다.')
    return answer