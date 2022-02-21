from collections import deque
def p_num(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nn(n, q):
    rev_base = ''
    if n == 10:
        return [str(num) for num in str(q)]
    
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10 and mod <= 16:
            rev_base += chr(mod+55)
        else:    
            rev_base += str(mod)
    if len(rev_base) == 0:
        return ['0']
    return list(str(rev_base[::-1]))

def solution(n, k):
    answer = 0
    trans_num = nn(n, k)
    print(trans_num)
    tmp = ""
    for i in range(len(trans_num)):
        if trans_num[i] != '0':
            tmp += str(trans_num[i])
        else:
            if tmp != '' and p_num(int(tmp)):
                print("tmp : ", tmp)
                print("ANS0 : ", answer)
                answer += 1
                print("ANS1 : ", answer)
            tmp = ""
    if tmp != '' and p_num(int(tmp)):
        print("ANS11 : ", answer)
        print("LAST :L ", tmp)
        answer += 1
        print("ANS22 : ", answer)
    return answer

n = 110011
k = 10
print(solution(n, k))