def solution(topping):
    answer = 0


    left_map = {}
    right_map = {}

    left_map[str(topping[0])] = 1
    for n in range(1, len(topping)):
        try:
            right_map[str(topping[n])] += 1
        except:
            right_map[str(topping[n])] = 1
    
    if len(left_map.keys()) == len(right_map.keys()):
        answer += 1
    
    for top in topping[1:]:
        try:
            left_map[str(top)] += 1
        except:
            left_map[str(top)] = 1
        right_map[str(top)] -= 1
        if right_map[str(top)] == 0:
            del right_map[str(top)]
        if len(left_map.keys()) == len(right_map.keys()):
            answer += 1

    return answer
