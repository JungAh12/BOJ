cnt = []
K = int(input())

def hanoi(n, f, b, t, cnt):
    if n==1:
        cnt.append((f, t))
    else:
        hanoi(n-1,f,t,b,cnt)
        cnt.append((f, t))
        hanoi(n-1,b,f,t,cnt)

hanoi(K,1,2,3,cnt)
print(len(cnt))
for i in range(len(cnt)):
    print(str(cnt[i][0])+' '+str(cnt[i][1]))
