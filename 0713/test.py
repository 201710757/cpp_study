from collections import deque

# def move_condition(x1, y1, x2, y2, board):
#     return not(board[x1][y1] or board[x2][y2])
def turn_condtion(x1, y1, x2, y2, board):
    condition = []
    rotate = [1, -1]
    if x1 == x2: # oo
        for r in rotate:
            if board[x1+r][y1] == 0 and board[x2+r][y2] == 0:
                condition.append([x1 + r, y1, x1, y1])
                condition.append([x2 + r, y2, x2, y2])
    else: # 8
        for r in rotate:    
            if board[x1][y1+r] == 0 and board[x2][y2+r] == 0:
                condition.append([x1, y1, x1, y1 + r])
                condition.append([x2, y2, x2, y2 + r])

    moving = [[1,0], [0,1], [-1,0], [0,-1]]
    for xx, yy in moving:
        if board[x1 + xx][y1 + yy] == 0 and board[x2 + xx][y2 + yy] == 0:
            condition.append([x1 + xx, y1 + yy, x2 + xx, y2 + yy])

    return condition


def solution(board):
    _board = [[1 for i in range(len(board)+2)] for i in range(len(board)+2)]
    for i in range(len(board)):
        for j in range(len(board)):
            _board[i+1][j+1] = board[i][j]
            
    x1, y1, x2, y2 = 1,1,1,2 # start idx 1
    # condition(x1,y1,x2,y2, board)
    que = deque()
    que.append([[x1,y1,x2,y2], 0])
    visited = []
    visited.append([x1,y1,x2,y2])

    while len(que) != 0:
        pos, cnt = que.popleft()
        cnt_1 = cnt+1

        # print(list(pos[:2]), list(pos[2:]))
        # if (len(board), len(board)) in list(pos[:2]):
        #     return cnt_1
        # if (len(board), len(board)) in list(pos[2:]):
        #     return cnt_1
        # if (pos[0] == len(board) and pos[1] == len(board))\
        #     or (pos[2] == len(board) and pos[3] == len(board)):
        #     return cnt_1

        # print(pos, cnt)
        # for xx1, yy1, xx2, yy2 in moving:
            # if move_condition(x1 + xx1, y1 + yy1, x2 + xx2, y2 + yy2, board):
            #     if not [x1 + xx1, y1 + yy1, x2 + xx2, y2 + yy2] in visited:
            #         que.append([[x1 + xx1, y1 + yy1, x2 + xx2, y2 + yy2], cnt_1])
            #         visited.append([x1 + xx1, y1 + yy1, x2 + xx2, y2 + yy2])

        moves = turn_condtion(pos[0], pos[1], pos[2], pos[3], _board)
        for q in moves:
            if (q[0] == len(board) and q[1] == len(board))\
                or (q[2] == len(board) and q[3] == len(board)):
                return cnt_1
            if not (q in visited):
                que.append([q, cnt_1])
                visited.append(q)
        # print(len(que))


    answer = 0
    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))