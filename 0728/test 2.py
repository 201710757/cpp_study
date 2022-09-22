from collections import deque
import copy # b = copy.deepcopy(a)
import numpy as np

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def solution(board, aloc, bloc):
    answer = []
    aloc[0] += 1
    aloc[1] += 1
    bloc[0] += 1
    bloc[1] += 1

    maximize = {}

    
    n_board = np.zeros([len(board)+2, len(board[0])+2])
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            n_board[i][j] = board[i-1][j-1]
    que = deque([])
    
    init_cnt = 0
    init_turn = 0 # 0:A, 1:B
    que.append([copy.deepcopy(n_board), aloc, bloc, init_turn, init_cnt])
    
    while len(que) != 0:
        board, a_loc, b_loc, turn, cnt = que.popleft()
        # if a_loc == b_loc:
        #     try:
        #         if maximize[tuple(a_loc+b_loc)] < cnt + 1:
        #             maximize[tuple(a_loc+b_loc)] = cnt + 1
        #     except:
        #         maximize[tuple(a_loc+b_loc)] = cnt + 1
        #     answer.append(cnt)
        if turn == 0: # move A
            END_FLAG = True
            ax, ay = a_loc
            for i in range(4):
                if board[ax + dx[i]][ay + dy[i]] != 0:
                    aloc = [ax+dx[i], ay+dy[i]]

                    b = copy.deepcopy(board)
                    b[ax][ay] = 0
                    END_FLAG = False

                    # if aloc == b_loc:
                    #     answer.append(cnt)
                    if aloc == b_loc:
                        print("aa ", tuple(aloc+b_loc), str(cnt+1))
                        try:
                            if maximize[tuple(aloc+b_loc)] < cnt + 1:
                                maximize[tuple(aloc+b_loc)] = cnt + 1
                        except:
                            maximize[tuple(aloc+b_loc)] = cnt + 1
                        # answer.append(cnt+1)
                    else:
                        que.append([b, aloc, b_loc, 1, cnt + 1])
            if END_FLAG:
                try:
                    if maximize[tuple(a_loc+b_loc)] < cnt:
                        maximize[tuple(a_loc+b_loc)] = cnt
                except:
                    maximize[tuple(a_loc+b_loc)] = cnt
                # answer.append(cnt)
            
        else: # move B
            END_FLAG = True
            bx, by = b_loc
            for i in range(4):
                if board[bx + dx[i]][by + dy[i]] != 0:
                    bloc = [bx+dx[i], by+dy[i]]

                    b = copy.deepcopy(board)
                    b[bx][by] = 0
                    END_FLAG = False

                    # if bloc == a_loc:
                    #     answer.append(cnt)
                    if a_loc == bloc:
                        print("bb ", tuple(a_loc+bloc), str(cnt+1))
                        try:
                            if maximize[tuple(a_loc+bloc)] < cnt + 1:
                                maximize[tuple(a_loc+bloc)] = cnt + 1
                        except:
                            maximize[tuple(a_loc+bloc)] = cnt + 1
                        # answer.append(cnt + 1)
                    else:
                        que.append([b, a_loc, bloc, 0, cnt + 1])
            if END_FLAG:
                try:
                    if maximize[tuple(a_loc+b_loc)] < cnt:
                        maximize[tuple(a_loc+b_loc)] = cnt
                except:
                    maximize[tuple(a_loc+b_loc)] = cnt
                # answer.append(cnt)
    # print(answer)
    print(maximize)
    print(maximize.values())
    return min(maximize.values())
    
    
    
# board=[[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
# aloc, bloc= [0, 0], [3, 3]

board=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc, bloc= [1, 0], [1,2]

# board=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# aloc, bloc= [1, 0], [1,2]

# board= [[1]]
# aloc, bloc=[0, 0], [0,0]


print(solution(board, aloc, bloc))