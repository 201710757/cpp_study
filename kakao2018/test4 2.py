# variable

MSG = "TOBEORNOTTOBEORTOBEORNOT"
# function
def solution(msg):
    answer = []
    dic = {}

    idx = 65
    while True:
        dic[chr(idx)] = idx-64
        if chr(idx) == 'Z':
            break  
        idx += 1
    idx -= 63
    
    tmp_idx = 0
    total_idx = 0
    while True:
        if total_idx >= len(msg)-1:
            break
        s_idx = ""
        
        for c in msg[total_idx:]:
            s_idx += c
            if s_idx in dic:
                total_idx += 1
            else:
                dic[s_idx] = idx
                idx += 1
                break

        if total_idx >= len(msg)-1:
            answer.append(dic[s_idx])
        else:
            answer.append(dic[s_idx[:-1]])
    

    return answer
print(solution(MSG))