N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

low = 0
high = 2000000000*30 #가장 오래걸리는 경우 최대 인원이 최대 시간 놀이기구 타는 경우(unsigned int 처리했다가 틀림)
c = 0
time = 0
# 마지막 친구가 언제 탔는지 시간 먼저 계산해야함
while low<=high:
    mid = (low+high)//2
    #맨 처음에는 다 탐
    c = M
    for i in range(M):
        c += mid//arr[i]
    if c>=N:    #애들이 너무 많음
        time = mid
        high = mid-1
    else:       #애들 늘려야함
        low = mid+1

# 마지막 친구가 자기 시간에 탄 놀이기구 번호를 계산해야함
# 처음엔 다 탐
ch = M
for i in range(M):
    ch += (time-1)//arr[i]# 마지막 친구가 탄 시간 직전 시간까지 해당 놀이기구에 탔던 사람 수 알 수 있음
for i in range(M):
    if time%arr[i] == 0:    #이때 탔다는 것
        ch+=1
    if ch==N:   #마지막 친구 차례가 왔으면
        print(i+1)  #0번부터니까 +1 해서 놀이기구 출력
        break

