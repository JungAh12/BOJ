import collections
import sys

NM = list(map(int, sys.stdin.readline().split(' ')))
cq = collections.deque([i+1 for i in range(NM[0])])
num = list(map(int, sys.stdin.readline().split(' ')))
sum = 0

while True:
    if not num:
        print(sum)
        break
    idx = cq.index(num[0])
    if cq[0] == num[0]:
        NM[0]-=1
        cq.popleft()
        del num[0]
    elif abs(-idx)<abs(NM[0]-idx):
        cq.rotate(-idx)
        sum+=abs(-idx)
    else:
        cq.rotate(NM[0]-idx)
        sum+=NM[0]-idx