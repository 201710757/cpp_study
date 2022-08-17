# 10 5 2 1 1
def solution(a, b, n):
    answer = 0

    tot = n
    while tot >= a:
        
        answer += int(tot/a)*b

        # tot -= (tot / a)
        left_ = int(tot%a)

        tot /= a
        tot = int(tot)*b
        tot += left_
        # print(tot)



    return answer



a = 3
b = 1
n = 20
print(solution(a,b,n))