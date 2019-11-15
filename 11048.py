import sys
sys.setrecursionlimit(100000)

def dp(board, n, m, state):
    ai=[n+1,n,n+1]
    aj=[m,m+1,m+1]
    nex = []
    if m >= M or n >= N:
        return 0
    if state[n][m] != -1:
        return state[n][m]
    for i,j in zip(ai, aj):
        nex.append(board[n][m]+dp(board, i, j,state))

    state[n][m] = max(nex)
    return state[n][m]

N, M = map(int, input().split(' '))
action_n = 3
board = []
for i in range(N):
    board.append(list(map(int, input().split(' '))))
state = [[-1]*M for i in range(N)]
print(dp(board, 0, 0, state))