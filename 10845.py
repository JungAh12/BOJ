instruction = int(input())

queue = []
ins = {}
for i in range(instruction):
    ins[i] = input().split(' ')

for i in range(instruction):
    if ins[i][0] == 'push':    # 정수 x 스택에 넣음
        queue.append(int(ins[i][1]))
    elif ins[i][0] == 'pop':   # 스택 가장 위 정수 출력 정수 없는 경우 -1
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif ins[i][0] == 'size':  # 스택 정수 개수 출력
        print(len(queue))
    elif ins[i][0] == 'empty': # 스택 비어있으면 1, 아니면 0 출력
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif ins[i][0] == 'front':   # 맨 위 꺼내고 출력, 없으면 -1
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif ins[i][0] == 'back':   # 맨 위 꺼내고 출력, 없으면 -1
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)