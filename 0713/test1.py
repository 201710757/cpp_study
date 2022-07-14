import numpy as np
from collections import deque

def solution(info, edges):
    answer = 0
    
    que = deque()

    board = np.zeros([len(info), len(info)])
    # board[0][0] = 1
    edges = [[0,0]] + edges
    for idx, [x,y] in enumerate(edges):
        d = -1 if info[idx] == 1 else 1
        board[x][y] = d
        print(x, y, d)
        # board[y][x] = d
    print(board)
    start_idx = 0
    que.append([start_idx, start_idx, board[start_idx][start_idx]])
    
    visit_list = deque()
    # visit_list.append(board[start_idx][start_idx])

    life = sum(visit_list)

    while len(que) != 0:
        print(que, visit_list)
        x, y = -1, -1
        max_val = -9876
        for q in que:
            v = q[2]
            if v > max_val and life + v > 0:
                max_val = v
                x, y = q[0], q[1]
        if x == -1 and y == -1:
            break
        else:
            visit_list.append(max_val)
            life += max_val
            print("appended : ", x, ", ", y, " life : ", life)
            que.remove([x, y, max_val])


        # if life + max_val > 0:
        #     life += max_val
        #     visit_list.append(max_val)
        # else:
        #     break

        print(que, visit_list)
        # print(max(map(que, lambda x:x[2])))
        print(x, y, max_val, life)
        for i in range(len(info)):
            if board[y][i] != 0 and y != i:
                if life + board[y][i] > 0:
                    life += board[y][i]
                    visit_list.append(board[y][i])
                    print("appended in : ", y, ", ", i, " life : ", life)

                    for j in range(len(info)):
                        if board[i][j] != 0:
                            que.append([i,j, board[i][j]])
                else:
                    que.append([y, i, board[y][i]])
    
    for v in visit_list:
        if v == 1:
            answer += v
    print(visit_list)
    return int(answer)


# info = [0,0,1,1,1,0,1,0,1,0,1,1]
info = [0,1,0,1,1,0,1,0,0,1,0]

# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(info, edges))