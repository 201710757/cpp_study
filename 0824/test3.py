from collections import deque

N = int(input())
K = int(input())

apple_pos = []
direction_info = []

for _ in range(K):
    tmp = input().split()
    apple_pos.append([int(tmp[0]), int(tmp[1])])

L = int(input())
for _ in range(L):
    tmp = input().split()
    direction_info.append([int(tmp[0]), tmp[1]])

dx = [0,1,0,-1]
dy = [-1,0,1,0]
# up right down left
dir = 1

body = deque([[0, 0]])

cnt = 0
for time, direction in direction_info:
    for _ in range(time):
        cnt += 1

        head = body[0]
        if [head[0] + dx[dir], head[1] + dy[dir]] in apple_pos:
            body.appendleft([head[0] + dx[dir], head[1] + dy[dir]])
        else:
            for i in range(len(body)):
                if [body[i][0] + dx[dir], body[i][1] + dy[dir]] in body \
                    or not (body[i][0] + dx[dir] >= 0 and body[i][0] + dx[dir] < N) \
                    or not (body[i][1] + dy[dir] >= 0 and body[i][1] + dy[dir] < N):
                    print(cnt)
                    import sys
                    sys.exit(0)
                body[i] = [body[i][0] + dx[dir], body[i][1] + dy[dir]]
        
    if direction == 'L':
        dir -= 1
    elif direction == 'D':
        dir += 1
    dir %= 4





