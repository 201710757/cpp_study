board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
m = 4
n = 5

answer = 0
    
_board = [[1]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        _board[i][j] = board[i][j]

_flag=True
while _flag:
    _flag=False
    res_set=set()
    for i in range(m-1):
        for j in range(n-1):
            if _board[i][j] == _board[i+1][j] == _board[i][j+1] == _board[i+1][j+1] != 0:
                res_set |= set([(i,j),(i+1,j),(i,j+1),(i+1,j+1)])
                _flag=True
    for i,j in res_set:
        _board[i][j] = 0
        answer+=1
    for i in range(m-1):
        for j in range(n):
            if _board[i+1][j] == 0 and _board[i][j] != 0:
                _board[i+1][j] = _board[i][j]
                _board[i][j] = 0
print(answer)