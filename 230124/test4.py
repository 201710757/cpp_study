import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()


board = []
def f(x, y, _start='B'):
    
    _cnt = 0 if _start == board[x][y] else 1
    # start = 'W' if board[x][y] == 'B' else 'B'

    # ori_start = board[x][y]
    # pick = ''

    for i in range(8):
        for j in range(8):
            # print(start, end = ' ')
            
            if i == 0 and j == 0 :
                start = _start
                continue
            # if i != 0:
            # print(i, j)
            if j != 0 :
                start = 'B' if 'W' == start else 'W'
            
            pick = board[i + x][j + y]
            # print(pick,)
            if start != pick:
                _cnt += 1
                # print("s : ", start, pick, i, j)
        start = 'W' if 'W' == start else 'B'
        # print("")

    
    return _cnt

N, M = map(int, sys.stdin.readline().split())

# board = [list]
for i in range(N):
    board.append("".join(list(map(str, sys.stdin.readline().split())))) 

_min = 987654321
# print("B : ", board[3])

for i in range(N-8+1):
    for j in range(M-8+1):
        # print("STart : ", i, j)
        for k in range(2):
            color = ['W', 'B']
            cnt = f(i, j, color[k])
            # print(cnt)
            if _min > cnt:
                # print(i, j, k, cnt)
                _min = cnt

# T
# _board = list(map(list, zip(*board)))
# print(board)
# print(_board)
# for i in range(M-8+1):
#     for j in range(N-8+1):
#         # print("STart : ", i, j)
#         cnt = f(i, j)
#         # print(cnt)
#         if _min > cnt:
#             _min = cnt
print(_min)
# print(board)

'''
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW
'''





