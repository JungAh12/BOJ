import sys

if __name__ == '__main__':
    N = sys.stdin.readline().rstrip()
    if int(N) < 10:
        N = '0'+N
    origin = N
    cnt = 0
    s = 0
    while True:
        s = 0
        s += int(origin[0])
        s += int(origin[1])
        origin = list(origin)
        origin[0] = origin[1]
        origin[1] = list(str(s))[-1]
        origin = ''.join(origin)
        cnt+=1
        if origin == N:
            break
    print(cnt)
  