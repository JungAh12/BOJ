from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)
time = [0 for _ in range(100001)]
path = [0 for _ in range(100001)]
ans = []

while q:
    v = q.popleft()
    if v == K:
        print(time[v])
        ans.append(str(K))
        while v!= N:
            ans.append(str(path[v]))
            v = path[v]
        
        ans = ans[::-1]
        print(' '.join(ans))
        break

    for next_step in (v-1, v+1, v*2):
        if 0<=next_step<100001 and time[next_step] == 0:
            time[next_step] = time[v]+1
            path[next_step] = v
            q.append(next_step)