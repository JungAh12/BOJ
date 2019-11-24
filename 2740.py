#분할정복안써도통과되는문제였음.. 분할정복으로 어떻게 풀 수 있지?
N,M = map(int, input().split(' '))
A = []
for _ in range(N):
    A.append(list(map(int, input().split(' '))))
M,K = map(int, input().split(' '))
B = []
for _ in range(M):
    B.append(list(map(int, input().split(' '))))

def mul():
    sub = 0
    for n in range(N):
        for k in range(K):
            for m in range(M):
                sub += A[n][m]*B[m][k]
            print(sub, end=' ')
            sub = 0
        print()
            
            
mul()
