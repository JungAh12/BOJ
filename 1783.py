N,M = map(int, input().split(" "))

if N==1:
    print(1)
elif N == 2:
    print(min(4,(M+1)//2))
else:
    if M < 7:
        print(min(4,M))
    elif M==7:
        print(5)
    else:
        print(M-2)
