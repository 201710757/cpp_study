import sys

def recursion(s ,l, r, cnt=0):
    if l>=r:
        return 1, cnt
    elif s[l] != s[r]: 
        return 0, cnt
    return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline()) #map(int, sys.stdin.readline().split())

a = []
b = []
inpu = []
for _ in range(N):
    inpu.append(str(sys.stdin.readline())[:-1])

for i in range(N):
    _a, _b = isPalindrome(inpu[i])
    a.append(_a)
    b.append(_b)

for i in range(len(a)):
    print(a[i], b[i])


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(N))