if __name__ == '__main__':
    N = int(input())
    x = input()
    sum = 0
    for i in range(N):
        sum += int(x[i])
    print(sum)