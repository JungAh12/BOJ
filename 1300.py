N=int(input())
M=int(input())

low = 1
high = M
ans = 0
while low<=high:
    mid = (low+high)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(mid//i,N)
    if cnt < M:
        low = mid+1
    else:
        ans = mid
        high = mid-1

print(ans)
