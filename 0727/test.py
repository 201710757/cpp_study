def solution(X, Y):
    save_num = []
    answer = ''

    X = list(X)
    # X.sort(reverse=True)
    Y = list(Y)
    # Y.sort(reverse=True)

    x_dict = {}
    y_dict = {}
    for _x in X:
        try:
            x_dict[str(_x)] += 1
        except:
            x_dict[str(_x)] = 1
    for _y in Y:
        try:
            y_dict[str(_y)] += 1
        except:
            y_dict[str(_y)] = 1

    y_key = list(y_dict.keys())
    for (k, v) in x_dict.items():
        if k in y_key:
            res = min(x_dict[k], y_dict[k])
            for _ in range(res):
                save_num.append(k)
    print(save_num)

    if len(save_num) > 0:
        res = ""
        # for idx in range(len(save_num)):
        #     save_num[idx] = int(save_num[idx])
        save_num.sort(reverse=True) # = sorted(save_num)
        if save_num[0] == '0':
            return "0"
        # for idx in range(len(save_num)):
        #     res += save_num[idx]
        res = ''.join(save_num)
    else: 
        return "-1"
    return res



X = "5525"
Y = "1255"
print(solution(X, Y))