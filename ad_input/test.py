from collections import deque
import time
# time.strftime('%H:%M:%S', time.gmtime(12345))
def hms_to_s(s):
    t = 0
    for u in s.split(':'):
        t = 60 * t + int(u)
    return t

def solution(play_time, adv_time, logs):
    log_arr = [0 for _ in range(360000)]
    answer = ''
    
    for log in logs:
        log = log.split('-')
        s = log[0]
        e = log[1]
        print(s, e)
        sec_e = hms_to_s(e)
        sec_s = hms_to_s(s)
        print(sec_s, sec_e)
        for i in range(sec_s, sec_e):
            log_arr[i] += 1
    print("AD : ", hms_to_s(adv_time))
    t = hms_to_s(adv_time)
    q = deque(log_arr[:t])
    print("len : ", len(q))
    tot=sum(q)
    print(tot)
    print(time.strftime('%H:%M:%S', time.gmtime(tot)))
    
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

play_time, adv_time, logs = "99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# "02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]
print(solution(play_time, adv_time, logs))
