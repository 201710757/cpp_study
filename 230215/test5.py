import sys
import itertools
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

N = int(input())

res = [0 for _ in range(N)]

global cnt
cnt = 0

def dfs(pos):
    global cnt
    if pos == N:
        cnt += 1
        return
        
    for i in range(N):
        res[pos] = i

        _flag = True
        for j in range(pos):
            if res[pos] == res[j] or pos-j == abs(res[pos] - res[j]):
                _flag = False
        if _flag:
            dfs(pos+1)


# def dfs(_n):
#     if len(res) == r:
#         for _r in res:
#             print(_r, end=' ')
#         print()
#         return
    
#     for i in range(_n, n+1):
#         # if i not in res:
#         res.append(i)
#         dfs(i)
#         res.pop()


dfs(0)
print(cnt)





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