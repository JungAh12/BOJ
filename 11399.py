N = int(input())
P = list(map(int,input().split(' ')))
P = sorted(P)
res = 0
for i in range(N):
    res += sum(P[:i+1])
print(res)