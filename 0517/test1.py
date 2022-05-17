dx = [-1,1,0,0, -11,11,0,0]
dy = [0,0,-1,1,  0,0,-11,11]
enter = [0, 1]
# 11, -11 : +Ctrl

def bfs(board, x, y, res=[], cnt=0, _cnt=[]):
    

    for e in enter:
        if e:
            res.append([board[x][y], x, y])
            board[x][y] = 99
            if len(res) == 2:
                if res[0][0] == res[1][0]:
                    board[res[0][1]][res[0][2]] = 0
                    board[res[1][1]][res[1][2]] = 0
                else:
                    board[res[0][1]][res[0][2]] = res[0][0]
                    board[res[1][1]][res[1][2]] = res[1][0]
                res = []
                
            cnt += 1
            
        for i in range(len(dx)):
            print(res)
            _flag = True
            _x = 0
            _y = 0
            print(x, y)
            if dx[i] == 11:
                _x = 1
                while True:
                    if x > 3 : break
                    if board[x][y] == 0:
                        _x += 1
                    else:
                        break
            elif dx[i] == -11:
                _x = 1
                while True:
                    if x < 0 : break
                    if board[x][y] == 0:
                        _x += 1
                    else:
                        break
            elif dy[i] == 11:
                _y = 1
                while True:
                    if y > 3 : break
                    if board[x][y] == 0:
                        _y += 1
                    else:
                        break
            elif dy[i] == -11:
                _y = 1
                while True:
                    if y < 0 : break
                    if board[x][y] == 0:
                        _y += 1
                    else:
                        break
            else:
                _flag = False
                if (x+dx[i] < 4 and x+dx[i]>=0) and (y+dy[i] < 4 and y+dy[i]>=0):
                    x = x+dx[i]
                    y = y+dy[i]
                    cnt += 1
                    # bfs(board, x + dx[i], y + dy[i], res, cnt+1, _cnt)
            if _flag:
                if (x+_x < 4 and x+_x>=0) and (y+_y < 4 and y+_y>=0):
                    x = x + _x
                    y = y + _y
                    cnt += 1
                    # bfs(board, x + _x, y + _y, res, cnt+1, _cnt)

    return min(_cnt)              
    
def solution(board, r, c):
    answer = 0
    cnt_list= []
    
    bfs(board, r, c, [], 0,cnt_list)
    return min(cnt_list)

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0

solution(board, r, c)