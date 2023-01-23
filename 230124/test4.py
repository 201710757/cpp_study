import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()


board = []
def f(x, y):
    
    _cnt = 0
    start = 'W' if board[x][y] == 'B' else 'B'
    pick = ''

    for i in range(8):
        for j in range(8):
            print(start, end = ' ')
            
            start = 'W' if 'B' == start else 'B'
            if i == 0 and j == 0 :
                continue
            # if i != 0:
            # print(i, j)
            
            pick = board[i + x][j + y]
            # print(pick,)
            if start != pick:
                _cnt += 1
                print("s : ", start, pick, i, j)
        start = 'W' if 'W' == pick else 'B'
        print("")

    
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
        cnt = f(i, j)
        # print(cnt)
        if _min > cnt:
            _min = cnt
print(_min)
# print(board)






