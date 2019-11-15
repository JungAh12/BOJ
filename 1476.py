import sys
En,Sn,Mn =  map(int,sys.stdin.readline().split(' '))
#1년이 지나면 각 1씩 증가
#범위를 넘으면 다시 1로
EE = 0
SS = 0
MM = 0
E = 1
S = 1
M = 1
while True:
    
    if E == En and S == Sn and M == Mn:
        if E==S==M==1:
            print(1)
            break
        print(EE+E)
        break
    
    E+=1
    S+=1
    M+=1

    if E > 15:
        EE += 15
        E = 1
    if S > 28:
        SS += 28
        S = 1
    if M > 19:
        MM += 19
        M = 1