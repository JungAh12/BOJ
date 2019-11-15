N = list(input())

if '0' not in N:
    print(-1)
    exit()
else:
    N = sorted(N, reverse = True)
    intN = [int(num) for num in N]
    if sum(intN)%3==0:
        print(''.join(N))
    else:
        print(-1)