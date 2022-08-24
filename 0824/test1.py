import numpy as np
from collections import deque
import copy

_in = input().split()
_list = []
for i in range(int(_in[0])):
    tmp = input()
    _list.append(tmp)


dx = [0,0,1,-1]
dy = [1,-1,0,0]
board = np.zeros([int(_in[0]), int(_in[1])])

blue = []
red = []
corr = []
for i, _l in enumerate(_list):
    idx = 0
    for l in _l:
        if l == '#':
            board[i][idx] = -1
        elif l == '.':
            board[i][idx] = 0
        elif l == 'B':
            blue = [i, idx]
            board[i][idx] = 1
        elif l == 'R':
            red = [i, idx]
            board[i][idx] = 2
        elif l == 'O':
            corr = [i, idx]
            board[i][idx] = 9
        idx += 1
print(board)
que = deque()

que.append([blue, red, copy.deepcopy(board), 0])
res = []
while que:
    b, r, _board, cnt = que.popleft()
    tmp_b = copy.deepcopy(b)
    tmb_r = copy.deepcopy(r)
    for i in range(4):
        _flag = True
        while _board[b[0] + dx[i]][b[1] + dy[i]] != -1 and _board[b[0] + dx[i]][b[1] + dy[i]] != 2:
            _board[b[0]][b[1]] = 0
            b = [b[0] + dx[i], b[1] + dy[i]]
            _board[b[0]][b[1]] = 1

            if corr == b:
                _flag = False

        while _board[r[0] + dx[i]][r[1] + dy[i]] != -1 and _board[r[0] + dx[i]][r[1] + dy[i]] != 1:
            _board[r[0]][r[1]] = 0
            r = [r[0] + dx[i], r[1] + dy[i]]
            _board[r[0]][r[1]] = 2

            if corr == r and _flag:
                res.append(cnt+1)
                continue
        if cnt+1 > 10 or (tmp_b == b and tmb_r == r):
            continue
        else:
            que.append([b, r, copy.deepcopy(_board), cnt+1])
            

        
print(res)