T = int(input())
for _ in range(T):
    S = input()
    S = S.split(' ')
    R = int(S[0])
    S = S[1]
    
    P = [i*R for i in S]
    for i in range(len(P)):
        print('{}'.format(P[i]),end='')
    print('')    