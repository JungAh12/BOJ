import sys
from collections import deque
N, K =  map(int,sys.stdin.readline().split(' '))

sis = K
pos_s = N
q = deque()
q.append(N)
time = [0 for i in range(100001)]

while q:
    v = q.popleft()
    if v == sis:
        print(time[v])
        break
    for next_step in (v-1, v+1, v*2): # dfs
        if 0<=next_step < 100001 and not time[next_step]:
            time[next_step] = time[v]+1
            q.append(next_step)