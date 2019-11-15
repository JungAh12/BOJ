if __name__ == '__main__':
    num = [0,0,0,0,0,0,0,0,0,0]
    c=1
    for _ in range(3):
        c *= int(input())
    
    c = list(str(c))
    for i in range(len(c)):
        c[i] = int(c[i])
        num[c[i]] += 1
    
    for i in range(len(num)):
        print(num[i])
        