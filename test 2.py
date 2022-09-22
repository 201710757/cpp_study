def solution(gems):
    answer = []
    unique_len = len(set(gems))
    gems_size = len(gems)
    
    temp = {}
    
    START = 0
    END = 0
    SE_len = 987654321
    
    for START, gem in enumerate(gems):
        
        while (END < gems_size) and (len(temp) < unique_len):
            if not gems[END] in temp:
                temp[gems[END]] = 0
            temp[gems[END]] += 1
            END += 1
            
        if len(temp) == unique_len:
            if SE_len > END - START:
                SE_len = END - START
                answer = [START + 1, END]
                #break
        temp[gem] -= 1
        if temp[gem] == 0:
            del temp[gem] # for check unique
    
    return answer




print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))



def solu1tion(gems):
    min_gems  = int(1e9)
    len_gems = len(gems) 
    n_gems = len(set(gems))
    end = 0
    temp = defaultdict(lambda : 0)
    for start, gem in enumerate(gems):
        while len(temp) < n_gems and end < len_gems: 
            temp[gems[end]] += 1
            end += 1
        if len(temp) == n_gems:
            if min_gems > end-start:
                min_gems = end-start
                result = [start+1, end]      
        temp[gem] -= 1
        if temp[gem] == 0:
            del(temp[gem])
    return result
