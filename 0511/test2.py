def solution(stones, k):
    _stones = sorted(stones)
    
    ans = 0
    for i in range(len(_stones)):
        if _stones[i] <= 0:
            continue
        stones = [s-_stones[i] for s in stones]
        ans += _stones[i]
        _stones = [s - _stones[i] for s in _stones]
        cnt = 0
        
        for j in range(len(stones)):
            if stones[j] <= 0:
                cnt += 1
            else:
                cnt = 0
                
            if cnt >= k:
                return ans
            

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3

print(solution(stones, k))