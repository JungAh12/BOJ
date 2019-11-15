res=[0 for _ in range(91)]
def fibo(x):
    if x >=3 :
        
        if res[x] != 0:
            return res[x]
        if res[x-1] != 0 and res[x-2] != 0:
            res[x] += res[x-1]
            res[x] += res[x-2]
            return res[x]
        return fibo(x-1)+fibo(x-2)
    return res[x]
if __name__ == "__main__":
    x = int(input())
    res[1]=1
    res[2]=1
    print(fibo(x))
