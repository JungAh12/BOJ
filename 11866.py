import sys
import collections

if __name__ == "__main__" :
    NK = list(map(int, sys.stdin.readline().split(' ')))

    q = collections.deque([i for i in range(1, NK[0]+1)])
    ans = []
    idx = 0
    while q:
        idx += NK[1]-1
        if idx >= len(q):
            idx = (idx%len(q))
            if idx == -1:
                idx = len(q)-1
        ans.append(q[idx])
        q.remove(q[idx])
    
    print(str(ans).replace('[', '<').replace(']','>'))
