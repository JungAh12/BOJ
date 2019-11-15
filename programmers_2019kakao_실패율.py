def solution(N, stages):
    answer = []
    fail = {}
    entry = len(stages)
    count = 0
    for i in range(N):
        curStage = i+1
        precount = count
        count = 0 
        for j in range(len(stages)):
            if stages[j] == curStage:
                count+=1
        entry -= precount
        if count != 0 and entry != 0:
            fail[curStage] = (count/entry)
        else :
            fail[curStage] = 0
    fail = sorted(fail.items(), key = (lambda x : x[1]), reverse=True)
    answer = [r[0] for r in fail]
    return answer