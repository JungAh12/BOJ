N = int(input())
board = [list(map(int, input().split(' '))) for _ in range(N)]
memo = [[0 for _ in range(N)]for _ in range(N)]

def dp(board, memo, i, j):
    if i>=N or j>=N:
        return 0
    if i<N-1 and j<N-1 and board[i][j] == 0:
        return 0
    if memo[i][j] != 0:
        return memo[i][j]

    if i==j==N-1 and board[i][j] == 0:
        return 1
    a = dp(board,memo, i, j+board[i][j])
    d = dp(board,memo, i+board[i][j], j)
    
    memo[i][j] = a+d
    return memo[i][j]

res = dp(board,memo, 0, 0)
print(res)