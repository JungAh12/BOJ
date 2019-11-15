def dp(memo, prev, now, steps):
    if now == 0:  # 시작은 계단으로 안친다.
        return 0
    if steps == 3:  # 연속 세 개 밟을 수 없음
        return 0
    if memo[prev][now]:    # 이미 계산한 것이라면
        #return memo[prev][now]
        pass
    else:
        if now-2 >= 0:
            a = dp(memo, now, now-1, steps+1)
            b = dp(memo, now, now-2, 1)
            memo[prev][now] = stepVal[now-1] + max(a,b)
        else:
            memo[prev][now] = stepVal[now-1] + dp(memo, now, now-1, steps+1)
            
    return memo[prev][now]


N = int(input())
stepVal = [int(input()) for i in range(N)]
memo = [[None for i in range(N+1)] for i in range(N+1)]
res = dp(memo, N, N, 1)
print(res)
