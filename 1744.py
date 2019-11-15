from collections import deque

N = int(input())
num = []
neg = []
pos = []
for _ in range(N):
    a = int(input())
    if a<=0:
        neg.append(a)
    else:
        num.append(a)

num = sorted(num)
neg = sorted(neg, reverse=True)
neg.extend(num)
num = neg
sum = 0
i = N-1
while i>=0:
    if i==0:
        sum+=num[i]
        i-=1
    else:
        if num[i]*num[i-1] <= num[i]:
            sum += num[i]
            i -= 1
        else:
            sum += num[i]*num[i-1]
            i -= 2
print(sum)
