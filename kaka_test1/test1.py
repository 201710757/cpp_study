import sys

answer = 0
n = 6
m = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]#['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
tmp_board = [[1]*n for i in range(m)]
#     _flag = False

#     while not _flag:
#         for i in range(m-1):
#             for j in range(n-1):
#                 if(board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]):
#                     _flag = True
#                 # tmp_board[i][j] = board[i][j]

#     tmp_board = board.copy()
_board = [[1]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        _board[i][j] = board[i][j]
        
_flag = True
cnttt = 0
while _flag:
    tmp_board = [[1]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            print(_board[i][j], end=" ")
        print('')
    print('')

    if cnttt == 2:
        sys.exit(0)

    
    for i in range(m-1):
        cmp = [b1 == b2 for b1, b2 in zip(_board[i], _board[i+1])]
        print(cmp)
        cnt = 1
        for j in range(len(cmp)-1):
            if cmp[j] == 1 and cmp[j+1] == 1 and _board[i][j] == _board[i][j+1]:
                cnt += 1
            elif cnt != 1:
                for k in range(cnt):
                    tmp_board[i][j-k] = 0
                cnt = 1
    for i in range(m):
        for j in range(n):
            print(tmp_board[i][j], end=" ")
        print('')
    print('')

    _flag = False           
    for i in range(m-1):
        for j in range(n):
            if tmp_board[i][j] == 0:
                _flag = True
                _board[i][j] = 0
                _board[i+1][j] = 0
    for i in range(m):
        for j in range(n):
            print(_board[i][j], end=" ")
        print('')
    print('')
    
    for i in range(m-1):
        for j in range(n):
            if _board[i+1][j] == 0:
                _board[i+1][j] = _board[i][j]
                _board[i][j] = 0
    cnttt += 1



for i in range(m):
    for j in range(n):
        print(_board[i][j], end=" ")
        if _board[i][j] == 0:
            answer += 1
    print("")
print(answer)
