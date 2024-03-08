import sys
from collections import defaultdict
import bisect
# N = int(sys.stdin.readline())
# list1 = [0 for _ in range(N + 1)]
# list2 = [0 for _ in range(N + 1)]
# for i in range(N):
#     c, p = map(int, sys.stdin.readline().split())
#     if c == 1:
#         list1[i + 1] = list1[i] + p
#         list2[i + 1] = list2[i]
#     else:
#         list1[i + 1] = list1[i]
#         list2[i + 1] = list2[i] + p
# # print(list1)
# # print(list2)
#
# Q = int(sys.stdin.readline())
# for i in range(Q):
#     l, r = map(int, sys.stdin.readline().split())
#     print(list1[r] - list1[l - 1],list2[r] - list2[l - 1])

# Q = int(sys.stdin.readline())
# q_list = []
# for i in range(Q):
#     l = list(map(int, sys.stdin.readline().split()))
#     q_list.append(l)
#
# for la, lb in q_list:

cost = [120, 150, 140, 110, 100]
kcal = [8, 10, 7, 6, 7]

dp = [[0 for j in range(31)] for i in range(5)]

# 一周目は簡単にわかりるので、わかる範囲から埋めていく
for i in range(31):
    if i >= kcal[0]:
        dp[0][i] = 120

# 二周目以降は以降は食べた場合と食べなかった場合を比較して埋めていく
for i in range(1, 5):
    for j in range(31):
        if kcal[i] > j:
            # カロリーオーバーで絶対食えない
            dp[i][j] = dp[i -1][j]
        else:
            # ここがポイントになりそう
            choice = dp[i - 1][j - kcal[i]] + cost[i]
            dp[i][j] = max(choice, dp[i -1][j])

print(dp[4][30])




# for i in range(1, 5):
#     print(i)

