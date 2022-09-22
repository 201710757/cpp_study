from collections import deque

def f(time):
    res = 0
    
    sp_time = time.split()
    
    main_time = sp_time[1]
    sec = float(sp_time[2][:-1]) * 1000
    
    up_point, down_point = main_time.split('.')
    
    up_h, up_m, up_s = up_point.split(':')
    mil_h = int(up_h) * 1000*60*60
    mil_m = int(up_m) * 1000*60
    mil_s = int(up_s) * 1000
    mil_down = int(down_point)
    mil_sec = int(sec)
    
    end_time = mil_h + mil_m + mil_s + mil_down
    start_time = end_time - mil_sec + 1
    return start_time, end_time


def solution(lines):
    answer = 0
    max_ans = -987654321
    deq = deque([])
    
    # lines = sorted(lines)
    lines = sorted(lines, key=lambda line : f(line)[0])
    for line in lines:
        s_mils, e_mils = f(line)
        answer = 1
        
        remove = 0
        if len(deq) != 0:
            for i in range(len(deq)):
                if s_mils - deq[i] < 1000: # millisec
                    answer += 1
                else:
                    remove += 1
                    # deq.popleft()
                    # break
        for i in range(remove):
            deq.popleft()
                    
        deq.append(e_mils)
        deq = deque(sorted(deq))
        if answer > max_ans:
            max_ans = answer
        
    
    return max_ans
inp = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print(solution(inp))