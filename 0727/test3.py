# 보조 : stack

from collections import deque


def solution(order):
    answer = 0

    sub = deque([])

    cnt = 0
    idx = 0
    box = 1
    while True:
        # print("Order : ", order[idx])
        if (len(sub)>0 and sub[-1] > order[idx]) or idx >= len(order):
            break
        if len(sub) > 0 and sub[-1] == order[idx]:
            sub.pop()
            answer += 1
            idx += 1
            box -= 1
        elif box == order[idx]:
            answer += 1
            idx += 1
        else:
            sub.append(box)
        box += 1
        if box > len(order):
            box = len(order)
            
        

    return answer

order = [5,4,3,2,1]

print(solution(order))
