import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline()) #map(int, sys.stdin.readline().split())


def fib(n):
    if n > 1:
        return n * fib(n-1)
    return 1

print(fib(N))