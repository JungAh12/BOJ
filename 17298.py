import sys
N = int(sys.stdin.readline()) 
seq = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1 for _ in range(N)] 
stack.append(0) 
i = 1 
while stack and i < N: 
    while stack and seq[stack[-1]] < seq[i]: 
        ans[stack[-1]] = seq[i] 
        stack.pop() 
    stack.append(i) 
    i += 1 
        
for i in range(N): 
    print(ans[i], end = " ")
