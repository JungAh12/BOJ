from collections import deque

def bfs(arr,visited,v):
    q = deque()
    q.append(v)
    visited[v] = True
    cnt = 0
    step = 0
    while q:
        if step == 2:
            break
        step += 1
        for _ in range(len(q)):
            v = q.popleft()
            for fr in arr[v]:
                if fr != 0:
                    if not visited[fr]:
                        visited[fr] = True
                        q.append(fr)
                        cnt += 1
        
    return cnt

if __name__=="__main__":
    n = int(input())
    m = int(input())
    arr = [[0]*(n+1) for _ in range(n+1)]
    visited = [False]*(n+1)

    for _ in range(m):
        i, j = map(int, input().split(' '))
        arr[i][j] = j
        arr[j][i] = i

    print(bfs(arr,visited,1))
