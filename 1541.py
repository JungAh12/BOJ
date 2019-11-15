form = input()
minusnum = ''
plusnum=''
isminus = False
sum = 0
for i in range(len(form)+1):
    if i >= len(form):
        if isminus:
            sum -= int(minusnum)
        else:
            sum += int(plusnum)
    else:
        if isminus:
            if form[i] == '+' or form[i] == '-':
                sum -= int(minusnum)
                minusnum=''
            else:
                minusnum += form[i]
        else:
            if form[i] == '+' or form[i]== '-':
                sum += int(plusnum)
                plusnum = ''
            if form[i] == '-':
                isminus = True
            elif form[i].isdigit:
                plusnum+=form[i]
print(sum)
        