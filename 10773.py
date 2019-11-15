K = int(input())
stack = []
for k in range(K):
    num = int(input())
    if num == 0:
        del stack[-1]
    else:
        stack.append(num)

print(sum(stack))