import sys

# N, M = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# data = sys.stdin.readline().rstrip()



N, M = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# s = set()
arr_str = {}
arr_idx = {}
# arr = []
for idx, i in enumerate(range(N)):
    _in = str(sys.stdin.readline())[:-1]
    arr_str[_in] = idx+1
    arr_idx[idx+1] = _in


res = []
for i in range(M):
    _in = str(sys.stdin.readline())[:-1]
    res.append(_in)

for r in res:
    if r.isalpha():
        print(arr_str[r])
    else:
        print(arr_idx[int(r)])




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


