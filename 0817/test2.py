from collections import deque

# 1,2,3,1
def solution(ingredient):
    answer = 0

    main_que = deque()
    # save_que = deque()

    for ing in ingredient:
        main_que.append(ing)

        if len(main_que) >= 4:
            tmp = [main_que[-4],main_que[-3],main_que[-2],main_que[-1]]
            if tmp[0] == 1 and tmp[1] == 2 and tmp[2] == 3 and tmp[3] == 1:
                answer += 1
                for _ in range(4):
                    main_que.pop()
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))