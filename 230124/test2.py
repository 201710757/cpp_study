import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

def f(n):
    arr = list(map(int, str(n)))
    
    return sum(arr) + n

# N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

# generator of 256 = 245
# generator of 216 = 198 and 207

res = 987654321

N = int(sys.stdin.readline())
for i in range(0, N):
    if f(i) == N and i < res:
        res = i

print(res) if res != 987654321 else print(0)