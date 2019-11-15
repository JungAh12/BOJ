N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr = sorted(arr)

high = arr[-1]
low = 0
def summation(arr, cut):
    res = 0
    for tree in arr:
        if cut > tree:
            continue
        res += tree-cut
    return res

while True:
    mid = (low+high)//2
    res = summation(arr, mid)
    if res == M:
        print(mid)
        exit()
    if high-1 <= low:
        break
    elif res > M:
        low = mid
    else:
        high = mid
print(mid)