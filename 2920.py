if __name__ == '__main__':
    c = input()
    c = c.split(' ')
    status = ''
    for i in range(len(c)-1):
        if c[i]>'8':
            status = "mixed"
            break
        if c[i]<c[i+1]:
            if status=='' or status=='ascending':
                status = "ascending"
            else:
                status = "mixed"
                break

        if c[i]>c[i+1]:
            if status=='' or status =='descending':
                status = "descending"
            else:
                status = "mixed"
                break

    print(status)