from collections import deque

def solution(want, number, discount):
    answer = 0
    discount_list = deque(discount[:10])
    _discount_list = deque(sorted(discount_list))

    for idx, n in enumerate(number):
        for _ in range(n-1):
            want.append(want[idx])
    want.sort()

    ok_flag = True
    for idx in range(len(want)):
        if want[idx] != _discount_list[idx]:
            ok_flag = False
            break
    if ok_flag:
        answer += 1

    for idx in range(10, len(discount)):
        discount_list.popleft()
        discount_list.append(discount[idx])

        _discount_list = deque(sorted(discount_list))
        print(_discount_list)
        print(want)
        ok_flag = True
        for i in range(len(want)):
            if want[i] != _discount_list[i]:
                ok_flag = False
                break
        if ok_flag:
            answer += 1


    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3,2,2,2,1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))