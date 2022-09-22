from collections import deque
import math

def f(start, end):
    _end = end.split(':')
    _start = start.split(':')
    
    end_h = int(_end[0])
    end_m = int(_end[1])
    start_h = int(_start[0])
    start_m = int(_start[1])
    
    if start_m > end_m:
        end_h -= 1
        end_m += 60
    
    return int((end_h - start_h) * 60 + (end_m - start_m))
    

def solution(fees, records):
    answer = []
    r = {}
    min_map = {}

    base_time = fees[0]
    base_fee = fees[1]
    unit_min = float(fees[2])
    unit_fee = fees[3]
    
    # math.ceil(3.14)
    
    for record in records:
        info = record.split()
        # print(info)
        if info[2] == "IN":
            r[str(info[1])] = str(info[0])
        elif info[2] == "OUT":
            minute = f(r[str(info[1])], str(info[0]))
            # minute -= 180
            
            _ = r.pop(str(info[1]))
            
            # fee = base_fee
            # if minute > 0:
            #     fee += math.ceil((minute / unit_min))*unit_fee
            if str(info[1]) in min_map:
                min_map[str(info[1])] += int(minute)
            else:
                min_map[str(info[1])] = int(minute)
            # print("MAP : :L ", min_map)
            
    if len(r) != 0:
        # print("R : ", r)
        for k, v in r.items():
            minute = f(r[str(k)], "23:59")
            # minute -= 180
            
            # fee = base_fee
            # if minute > 0:
            #     fee += math.ceil((minute / unit_min))*unit_fee
            if str(k) in min_map:
                min_map[str(k)] += int(minute)
            else:
                min_map[str(k)] = int(minute)

    # print(min_map)
    sorted_map = sorted(min_map.items())
    # print(sorted_map)
    for k in sorted_map:
        fee = base_fee
        map_m = k[1] - 180
        if map_m > 0:
            fee += int(math.ceil((k[1]-180)/unit_min)*unit_fee)
        answer.append(fee)
    return answer
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))