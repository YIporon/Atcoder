import sys
from collections import defaultdict
import math


# 平方数で割り続ける
# def divide_square(n):
#     if n == 1:
#         return 1
#     for i in range(2, int(math.sqrt(n)) + 1):
#         square = i * i
#         while n % square == 0:
#             n //= square
#             if n == 1:
#                 return 0
#     return n
#
#
# N = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))
#
# dictionary = defaultdict(int)
# for number in l:
#     if number != 0:
#         n = divide_square(number)
#         dictionary[n] += 1
#
# zero_count = l.count(0)
# pair_count = zero_count * (N - zero_count) + zero_count * (zero_count - 1) // 2
# for n, count in dictionary.items():
#     if n == 1:
#         # 1と平方数との積は必ず平方数となる
#         pair_count += count * dictionary[0]
#     pair_count += count * (count - 1) // 2

print(math.sqrt(25))
