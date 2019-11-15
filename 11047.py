N, K = map(int, input().split(' '))
val = [int(input()) for _ in range(N)]
num = 0

for i in range(N-1, -1, -1):
    if val[i] > K:
        continue
    num += K//val[i]
    K = K % val[i]

print(num)