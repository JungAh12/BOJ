N = int(input())
meeting = [[None, None] for i in range(N)]
for idx in range(N):
    meeting[idx][1], meeting[idx][0] = map(int, input().split(' '))

meeting = sorted(meeting, key=lambda x:[x[0],x[1]])
cnt = 0
cursec = -1
for i in range(N):
    if cursec <= meeting[i][1]:
        cursec = meeting[i][0]
        cnt+=1

print(cnt)