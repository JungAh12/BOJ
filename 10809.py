x = input()
alpha = [-1 for _ in range(26)]
for i in range(len(x)):
    if alpha[ord(x[i])-ord('a')] == -1 :
        alpha[ord(x[i])-ord('a')] = i
for i in range(len(alpha)):
    print('{} '.format(alpha[i]), end='')
