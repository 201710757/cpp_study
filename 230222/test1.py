import sys
import itertools
# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()

# board = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

# n, r = map(int, sys.stdin.readline().split())

n = int(input())
global r_n, d_n
r_n = 0
d_n = 0

def req_fib(n):
    global r_n
    if n == 1 or n == 2:
        r_n += 1
        return 1
    return req_fib(n-1) + req_fib(n-2)
    
def dyn_fib(n):
    global d_n
    fib_arr = [1, 1]
    for _ in range(2, n):
        fib_arr[-1] = fib_arr[1] + fib_arr[0]
        d_n += 1


# req_fib(n)
dyn_fib(n)

print(req_fib(n), d_n)