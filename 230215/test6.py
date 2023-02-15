import sys
import itertools
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

N = int(input())
number = list(map(int, sys.stdin.readline().split()))
calc = list(map(int, sys.stdin.readline().split()))

calc_info = [0 for _ in range(11)]

# print(N)
# print(number)
# print(calc)

global _max
global _min
_max = -987654321
_min = 987654321

def dfs(n):
    global _max
    global _min
    if n == N:
        res = number[0]

        for i in range(1, N):
            if calc_info[i] == 0:
                res += number[i]
            elif calc_info[i] == 1:
                res -= number[i]
            elif calc_info[i] == 2:
                res *= number[i]
            elif calc_info[i] == 3:
                if res < 0:
                    res = -res // number[i]
                    res = -res
                else:
                    res = res // number[i]

        if res > _max: _max = res
        if res < _min: _min = res

        return

    else:
        for i in range(4):
            if calc[i] == 0:
                continue
            calc[i] -= 1
            calc_info[n] = i

            dfs(n+1)

            calc_info[n] = 0
            calc[i] += 1



dfs(1)
print(int(_max))
print(int(_min))





'''
ans = itertools.combinations([(i+1) for i in range(n)], r)

for a in ans:
    if len(a) <= 1:
        print(a[0])
    else:
        for _a in a:
            print(_a, end=' ')
        print()
'''

########