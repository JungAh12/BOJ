def solution(n, arr1, arr2):
    arr = []
    for i in range(n):
        arr.append(arr1[i]|arr2[i])
        arr[i] = bin(arr[i]).replace('0b','')
    print(arr)
    for i in range(len(arr)):
        if len(arr[i])!=n:
            zero = '0'*(n - len(arr[i]))
            arr[i] = zero + arr[i]
        arr[i] = arr[i].replace("1","#")
        arr[i] = arr[i].replace("0"," ")
        
    return arr