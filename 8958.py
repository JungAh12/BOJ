if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        c = input()
        total=[0,0]
        for i in range(len(c)):
            if c[i]=='O':
                total[0]+=1
                total[1]+=total[0]
            else:
                total[0] = 0
        print(total[1])