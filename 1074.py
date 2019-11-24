##pypy3으로 실행
N,r,c = map(int, input().split(' '))
count = 0

def divide(size, x, y):
    global count
    if size <= 2:
        if(x==r and y==c):
            print(count)
            return
        count+=1
        if(x==r and y+1==c):
            print(count)
            return
        count+=1
        if(x+1==r and y==c):
            print(count)
            return
        count+=1
        if(x+1==r and y+1==c):
            print(count)
            return
        count+=1
        return

    divide((size//2), x,y)            ## size-1로 하면 index 이동할때 계산 불편
    divide((size//2), x,y+(size//2))
    divide((size//2), x+(size//2),y)
    divide((size//2), x+(size//2),y+(size//2))

if __name__=="__main__":
    divide(2**N,0,0)
