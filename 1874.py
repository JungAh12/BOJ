import sys
import collections

n = int(sys.stdin.readline())
#stack = collections.deque([i for i in range(1, n+1)])
stack = collections.deque()
ans = ''
idx = 0
for i in range(n):
    num = int(input())
    while idx < num:
        if num >= idx:
            idx+=1  
            ans+='+\n'
            stack.append(idx)
    while stack and stack[-1] == num:
    #if stack and stack[-1] == num:
        ans+='-\n'
        stack.pop()
        continue
if not stack :
    print(ans.rstrip())
else:
    print("NO")
            
        #top이 숫자와 같으면 팝