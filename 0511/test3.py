from collections import deque
import time
import numpy as np
# time.strftime('%H:%M:%S', time.gmtime(12345))

def hms_to_s(s):
    t = 0
    for u in s.split(':'):
        t = 60 * t + int(u)
    return t

def solution(play_time, adv_time, logs):
    log_arr = np.zeros(360000, dtype=np.int32)#[0 for _ in range(360000)]
    answer = ''
    
    for log in logs:
        log = log.split('-')
        s = log[0]
        e = log[1]
        # print(s, e)
        sec_e = hms_to_s(e)
        sec_s = hms_to_s(s)
        # print(sec_s, sec_e)
        
        log_arr[sec_s] += 1
        log_arr[sec_e] -= 1
        # for i in range(sec_s, sec_e):
        #     log_arr[i] += 1
    for i in range(1,len(log_arr)):
        log_arr[i] = log_arr[i] + log_arr[i-1]
            
    # print("AD : ", hms_to_s(adv_time))
    t = hms_to_s(adv_time)
    q = deque(log_arr[:t])
    # print("len : ", len(q))
    tot=np.sum(q)
    # print(tot)
    # print(time.strftime('%H:%M:%S', time.gmtime(tot)))
    
    _min = tot
    first = "00:00:00"
    for i in range(t, hms_to_s(play_time)):
        q.append(log_arr[i])
        tot += log_arr[i]
        tot -= q.popleft()
        # q.pop()
        
        if tot > _min:
            _min = tot
            first = time.strftime('%H:%M:%S', time.gmtime(i-t+1))
            # print(q)    
    
    return first
def _solution(play_time, adv_time, logs):
    log_arr = np.zeros(360000, dtype=np.int32)#[0 for _ in range(360000)]
    answer = ''
    
    for log in logs:
        log = log.split('-')
        s = log[0]
        e = log[1]
        # print(s, e)
        sec_e = hms_to_s(e)
        sec_s = hms_to_s(s)
        # print(sec_s, sec_e)
        
        log_arr[sec_s] += 1
        log_arr[sec_e] -= 1
        # for i in range(sec_s, sec_e):
        #     log_arr[i] += 1
        
    for i in range(1, len(log_arr)):
        log_arr[i] = log_arr[i] + log_arr[i-1]
    for i in range(1, len(log_arr)):
        log_arr[i] = log_arr[i] + log_arr[i-1]
            
    # print("AD : ", hms_to_s(adv_time))
    t = hms_to_s(adv_time)
    most_view = 0
    max_time = 0
    for i in range(t-1, hms_to_s(play_time)):
        if i >= hms_to_s(adv_time):
            if most_view < log_arr[i] - log_arr[i - hms_to_s(adv_time)]:
                most_view = log_arr[i] - log_arr[i - hms_to_s(adv_time)]
                max_time = i - hms_to_s(adv_time) + 1
        else:
            if most_view < log_arr[i]:
                most_view = log_arr[i]
                max_time = i - hms_to_s(adv_time) + 1
    return str(max_time)

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))