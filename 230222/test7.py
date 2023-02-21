import sys
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

N = int(input())
# board = list(map(int, sys.stdin.readline().split()))

cnt = 0
cache = [[0]*9 for _ in range(N)]
for i in range(9):
    cache[0][i] = 1

#for i in range(1, N):
#    for j in range(10):
#        #j==0 / j==9 / else

print(sum(cache[N-1]))