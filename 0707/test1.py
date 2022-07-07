board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]] 
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
import numpy as np
def solution(board, skill):
    answer = 0
    cum_board = np.zeros([len(board)+1, len(board[0])+1])#[[0] * (len(board[0])+1)] * (len(board)+1)
    
    for sk in skill:
        update = 1 if sk[0] == 2 else -1
        
        dmg = sk[5] * update
        # print(dmg)
        print("b ", cum_board[sk[1]][sk[2]])
        cum_board[sk[1]][sk[2]] += (dmg)
        print("a ", cum_board[sk[1]][sk[2]])
        
        cum_board[sk[3]+1][sk[2]] += (-dmg)
        
        cum_board[sk[1]][sk[4]+1] += (-dmg)
        cum_board[sk[3]+1][sk[4]+1] += (dmg)
    
        for i in range(len(cum_board)):
            for j in range(len(cum_board[0])):
                print(cum_board[i][j], end=' ')
            print("")
        print("dd")


    for i in range(len(board)):
        for j in range(len(board[0])):
            cum_board[i][j+1] += cum_board[i][j]
    for i in range(len(board[0])):
        for j in range(len(board)):
            cum_board[j+1][i] += cum_board[j][i]
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += cum_board[i][j]

            
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] >= 1:
                answer += 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print("")
    print("")
    return answer

print(solution(board, skill))