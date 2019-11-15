def solution(p):
    if p == '':
        return ''
    closen = 0
    openn = 0
    a = ''
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            openn +=1
            a+=p[i]
        elif p[i] == ')':
            openn -=1
            a+=p[i]
        if openn==0:
            if u=='':
                u += a
                a = ''
            elif u!='':
                v += a
                a = ''
    openn = 0
    closen = 0
    for i in range(len(u)):
        if u[i] == '(':
            openn += 1
        elif u[i] == ')':
            openn -= 1
        if openn < 0:
            c = ''+'('
            res = solution(v)
            c+=res
            c+=')'
            u = u[1:]
            u = u[:-1]
            u = list(u)
            for i in range(len(u)):
                if u[i] == '(':
                    u[i] = ')'
                elif u[i] == ')':
                    u[i] = '('
            u = ''.join(u)
            c+=u
            return c
        if openn == 0:
            u+=solution(v)
            return u