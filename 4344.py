import sys

if __name__ == '__main__':
    T = sys.stdin.readline().rstrip()
    for _ in range(int(T)):
        score = sys.stdin.readline().rstrip()
        score = score.split(' ')
        student = int(score[0])
        
        score_sum = 0
        for i in range(1, len(score)):
            score_sum+=int(score[i])    
        score_sum = score_sum/student

        st=student
        for i in range(1, len(score)):
            if score_sum >= int(score[i]):
                st-=1
        avg = round(float((st/student)*100),3)
        print('%.3f%s' %(avg,'%'))