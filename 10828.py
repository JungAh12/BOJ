instruction = int(input())

stack = []
ins = {}
for i in range(instruction):
    ins[i] = input().split(' ')

for i in range(instruction):
    if ins[i][0] == 'push':    # 정수 x 스택에 넣음
        stack.insert(0,int(ins[i][1]))
    elif ins[i][0] == 'top':   # 스택 가장 위 정수 출력 정수 없는 경우 -1
        if len(stack) != 0:
            print(stack[0])
        else:
            print(-1)
    elif ins[i][0] == 'size':  # 스택 정수 개수 출력
        print(len(stack))
    elif ins[i][0] == 'empty': # 스택 비어있으면 1, 아니면 0 출력
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ins[i][0] == 'pop':   # 맨 위 꺼내고 출력, 없으면 -1
        if len(stack) != 0:
            print(stack.pop(0))
        else:
            print(-1)



    