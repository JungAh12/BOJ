import sys
sys.setrecursionlimit(10**8)

n = int(input())
inorder = list(map(int, input().split(' ')))
postorder = list(map(int, input().split(' ')))
pre = []
pos = [0]*n
root = postorder[-1]

for i in range(n):
    pos[inorder[i]-1] = i

def divide(in_start, in_end, post_start, post_end):
    if (in_start > in_end or post_start > post_end):
        return # 탈출 조건 start가 end 넘으면 노드 1개일 때 경우 지난 것.

    root = postorder[post_end]-1    # pos가 0부터 시작이라서
    pre.append(root+1)  # 모든 노드는 root가 한번씩 된다.(leaf는 nil가진 parent라고 볼 수 있음)
    in_root = pos[root]
    left_s = in_root-in_start
    divide(in_start, pos[root]-1, post_start, post_start+left_s-1)
    divide(pos[root]+1, in_end, post_start+left_s, post_end-1)

divide(0,n-1,0,n-1)

for i in pre:
    print(i, end=' ')
    
    
# 코드 짧게  
'''
import sys
sys.setrecursionlimit(10**8)

n = int(input())
inorder = list(map(int,input().split(' ')))
postorder = list(map(int,input().split(' ')))
pos=[0]*(n+1)
for i in range(n):
    pos[inorder[i]] = i

def divide(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    root = postorder[post_end]
    print(root, end=' ')

    divide(in_start, pos[root] - 1, post_start, post_start + pos[root] - in_start - 1)
    divide(pos[root] + 1, in_end, post_start + pos[root] - in_start, post_end - 1)

divide(0, n - 1, 0, n - 1)
'''
