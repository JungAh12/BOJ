import sys
import collections

N = int(sys.stdin.readline())
deque = collections.deque()

for i in range(N):
    ins = sys.stdin.readline().rstrip().split(' ')
    if ins[0] == 'push_front':
        deque.appendleft(ins[1])
    elif ins[0] == 'push_back':
        deque.append(ins[1])
    elif ins[0] == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque.popleft())
    elif ins[0] == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif ins[0] == 'size':
        print(len(deque))
    elif ins[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif ins[0] == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif ins[0] == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])
            
