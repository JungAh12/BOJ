if __name__ == '__main__':
    x = input()
    x = x.split(' ')
    cnt=0
    for g in range(len(x)):
        if (g==0 or g==len(x)-1) and x[g]=='':
            continue
        cnt+=1
    print(cnt)