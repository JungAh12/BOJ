import sys

if __name__ == '__main__':
    T = sys.stdin.readline().rstrip()
    for i in range(int(T)):
        x = sys.stdin.readline().rstrip()
        x = x.split(' ')
        sum = 0
        for j in range(len(x)):
            sum += int(x[j])
        print(sum)