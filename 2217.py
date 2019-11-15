N = int(input())
rope = [int(input()) for _ in range(N)]
rope = sorted(rope)
result = 0
for i in range(1, N+1):
    result = max(result, i * rope[-i])
print(result)