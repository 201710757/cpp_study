import re

n = 16
t = 16
m =2 
p = 2
result="0111"
from collections import deque

def nn(n, q):
    rev_base = ''
    


    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10 and mod <= 16:
            rev_base += chr(mod+55)
        else:    
            rev_base += str(mod)
    if len(rev_base) == 0:
        return ['0']
    return list(str(rev_base[::-1]))


def solution(n, t, m, p):
    answer = ''
    
    num = 0
    s_num = []
    idx = 0
    while len(answer)<t:
        idx += 1 # start
        
        if len(s_num) == 0: # get number
            s_num = deque(nn(num, n))
            num += 1
        
        call = s_num.popleft()
        if (idx-1) % m == p-1:
            answer += call      
    return answer
# print(nn(16,10))
print(solution(n,t,m,p))