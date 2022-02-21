from itertools import combinations_with_replacement

def f(n, r):
    res = []
    lst = [x for x in range(n)]

    for cwr in combinations_with_replacement(lst, r):
        tmp = [0 for _ in range(11)]
        for idx in cwr:
            tmp[idx] += 1
        res.append(tmp)
    return res

# f(11, 5) = 11PI5
def trans(line):
    res = ""

    for i in range(len(line)):
        res += str(line[len(line)-1 -i])

    return int(res)

def solution(n, info):
    answer = []
    rep_comb = f(11, n)
    # print(rep_comb)
    
    max_lion_score = -987654321
    for comb in rep_comb:
        # print(comb)
        apch_score, lion_score = 0, 0
        for i in range(len(info)):
            if info[i] < comb[i]: # comb == lion
                lion_score += int(10-i)
            elif info[i] > 0:
                apch_score += int(10-i)
                
        if apch_score < lion_score:
            if max_lion_score < lion_score:
                max_lion_score = lion_score
                answer = [comb]
            elif max_lion_score == lion_score:
                answer.append(comb)
                
            # print("APCH : {} / LION : {}".format(apch_score, lion_score))
        # print(comb)
    
    if len(answer) == 0:
        answer = [-1]
    elif len(answer) >= 1:
        answer = sorted(answer, key=lambda _list : trans(_list), reverse=True)[0]
        
    return answer



_n = 5
_info = [2,1,1,1,0,0,0,0,0,0,0]	
print(solution(_n, _info))