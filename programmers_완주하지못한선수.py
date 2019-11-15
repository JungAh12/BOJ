def solution(p, c):
    dic = {}
    for i in p:
        if dic.get(i) is None:
            dic[i] = 0
        dic[i]+=1

    for i in c:
        if dic.get(i) is not None:
            dic[i] -=1
            if dic[i] == 0 :
                del dic[i]
    answer = list(dic.keys())[0]
    return answer