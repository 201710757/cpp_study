

from calendar import week

n = 200
weak = [0, 10, 50, 80, 120, 160]#[0,100]#[1,5,6,10] #[10, 0] [1,2] 12
dist = [1, 10, 5, 40, 30]#[1,1]
from itertools import permutations

def solution(n, weak, dist):
    answer = []
    
    ori_weak = weak + weak
    rev_wek = list(reversed(ori_weak))
    p_dist = list(permutations(dist, len(dist)))

    weak_N = len(weak)
    for i in range(len(weak)):
        for dist in p_dist:
            
            s = i
            e = i+1
            ans = 0
            repaired = 0
            for d in reversed(dist):
                while True:
                    if ori_weak[s] - ori_weak[e] < 0:
                        _dist = abs(ori_weak[s] - ori_weak[e])
                    else:
                        _dist = n - (ori_weak[s] - ori_weak[e])
                    if _dist <= d: 
                        e += 1
                    else:
                        repaired += e-s
                        s = e
                        e = s + 1
                        ans += 1
                        break
                if s >= len(weak):
                    if repaired == weak_N:
                        answer.append(ans)
                    ans = 0
                    break
                
    for i in range(len(weak)):
        for dist in p_dist:
            
            s = i
            e = i+1
            ans = 0
            repaired = 0
            for d in reversed(dist):
                while True:
                    if rev_wek[s] - rev_wek[e] >= 0:
                        _dist = rev_wek[s] - rev_wek[e]
                    else:
                        _dist = n - abs(rev_wek[s] - rev_wek[e])

                    if _dist < d: 
                        e += 1
                    else:
                        repaired += e-s
                        s = e
                        e = s + 1
                        ans += 1
                        break
                    if n-repaired == abs(s-e):
                        ans += 1
                        s += 1
                        break
                if s >= len(weak):
                    if repaired == weak_N:
                        answer.append(ans)
                    ans = 0
                    break
                
    return min(answer) if len(answer)>0 else -1

print(solution(n,weak, dist))


# 10,9,4,3,1,10,9,4,3,1
#