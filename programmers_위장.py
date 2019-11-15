def solution(clothes):
    clothes_dict = {}
    # 조합 공식 nCr = n!/r!(n-r)! 순서x 중복x
    # 순열 공식 nPr = n!/(n-r)! 순서o 중복x
    for i in range(len(clothes)):
        if not(clothes[i][1] in clothes_dict.keys()):
            clothes_dict[clothes[i][1]] = 1
        else:
            clothes_dict[clothes[i][1]] += 1
    ##print(clothes_dict)
    #kindnum = len(list(clothes_dict.keys()))
    clothesnum = list(clothes_dict.values())
    out = 1
    for i in range(len(clothesnum)):
        out *= clothesnum[i]+1

    out -= 1
    return out