
def ok(board1, board2):
    for i in range(len(board1)):
        for j in range(len(board1)):
            if baord1[i][j] != board2[i][j]:
                return False
    return True

def solution(beginning, target):
    answer = 0

    for i in range(len(beginning)):
        for j in range(len(beginning)):
            


    return answer



beginning, target = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

print(solution(beginning, target))