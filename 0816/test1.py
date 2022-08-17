def solution(number):
    answer = 0

    for i in range(len(number)):
        for j in range(len(number)):
            for k in range(len(number)):
                if i>j and j>k:
                    tot = number[i] + number[j] + number[k]
                    if tot == 0:
                        answer += 1


    return answer
