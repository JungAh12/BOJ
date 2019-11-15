import sys

if __name__ == '__main__':
    T = sys.stdin.readline().rstrip()
    score = sys.stdin.readline().rstrip()
    score = score.split(' ')
    tmp = -1
    score_sum = 0
    for i in range(int(T)):
        score_sum+=int(score[i])
        if tmp <= int(score[i]):
            tmp = int(score[i])
    
    score_sum = (score_sum/int(T))/tmp*100

    print('%f' %score_sum)