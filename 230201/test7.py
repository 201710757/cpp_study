import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()



_in = str(sys.stdin.readline())
s = set()
res = 0

for i in range(len(_in)):
    for j in range(len(_in) - (i+1)):
        s.add(_in[j:j+i+1])


print(len(s))


# M = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# for a in arr:
#     if a in s:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# # _max = -987654321

# # for i in range(N):
# #     for j in range(N):
# #         for k in range(N):
# #             if i == j or j == k or i == k:
# #                 continue
# #             pick = arr[i] + arr[j] + arr[k]
# #             if pick <= M and _max < pick:
# #                 _max = pick
        



# # print(_max)


