N, C = map(int, input().split(' '))
arr = []
for _ in range(N):
    arr.append(int(input()))
arr = sorted(arr)
mini = 1
maxi = arr[-1]-arr[0]

while mini<=maxi:
    mid = (maxi+mini)//2
    cnt = 1 # 맨 왼쪽에 하나 설치하고 시작해야함
    start = arr[0]
    #배열안에 공유기 다 설치되는지 확인
    for i in range(1,N):
        if(arr[i]-start>=mid):
            start = arr[i]
            cnt += 1
    
    if cnt >= C: # 공유기가 더 많이 설치됐으면 간격을 늘려야함
        ans = mid
        mini = mid+1
    else:   # 공유기 적게 설치됨 간격 좁히자
        maxi = mid-1

print(ans)
