result = [0,0,0]
N = int(input())
arr = [list(map(int, input().split(' '))) for i in range(N)]

def check(x,y,N):
    first = arr[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if arr[i][j] != first:
                return False, first
    return True, first

def slice(x, y, N):
    same, first = check(x,y,N)
    if same:
        result[first+1] += 1
        return

    n = N//3
    for i in range(0,3):
        for j in range(0,3):
            slice(x+i*n,y+j*n,n)  //이 부분을 계산을 잘해야함. 칸 옮기고 줄여나가는 

slice(0,0,N)

print(result[0])
print(result[1])
print(result[2])

