def f(start, n):
    res = []
    for i in range(start,start+n):
        res.append(i)
    print(res)
    return res

def solution(distance, scope, times):
    answer = []

    for idx in range(len(scope)):
        _times = times[idx]
        _scope = f(min(scope[idx]) % sum(_times), abs(scope[idx][1] - scope[idx][0])+1)
        # 3, 4 / 2, 2
        # 5,6,7,8 / 4,3
        for i in range(len(_scope)):
            if _scope[i] % sum(_times) > 0 and _scope[i] / sum(_times) >= 1 :
                _i = 1 if i >= len(_scope) else 1
                answer.append(scope[idx][0] + i)
                break

    return min(answer) if len(answer) > 0 else distance

distance, scope, times = 10, [[3, 4], [5, 8]], [[2, 5], [4, 3]]#12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]]
print(solution(distance, scope, times))