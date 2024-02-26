import sys
from itertools import product
from collections import defaultdict, Counter
import math

from collections import defaultdict
import math

read = sys.stdin.readline
# nを素因数分解したリストを返す
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def sieve_of_eratosthenes(x):
  nums = [i for i in range(x+1)]

  root = int(pow(x, 0.5))
  for i in range(2 ,root + 1):
    if nums[i] != 0:
      for j in range(i, x+1):
        if i*j >= x+1:
          break
        nums[i*j] = 0

  return set(nums)


# エラトステネスの篩を使用して最小の素因数を求める関数
def sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


# 素因数分解を行い、各素因子の指数が奇数のものだけを取り出す関数
def factorize(n, spf):
    factors = defaultdict(int)
    print("n=", n)
    while n > 1:
        factors[spf[n]] += 1
        n //= spf[n]
    print(factors)
    return [p for p, exp in factors.items() if exp % 2 == 1]


N = int(read())
A = list(map(int, read().split()))

print(sieve_of_eratosthenes(N))




# メインの処理
# def count_squareful_pairs(A, N):
#     spf = sieve(max(A))
#     print(spf)
#     factor_count = defaultdict(int)
#     zero_count = 0
#
#     for a in A:
#         if a == 0:
#             zero_count += 1
#             continue
#         pattern = tuple(sorted(factorize(a, spf)))
#         print('pattern', pattern)
#         factor_count[pattern] += 1
#
#     print('factor_count', factor_count)
#     count = zero_count * (N - zero_count) + zero_count * (zero_count - 1) // 2
#     for k, v in factor_count.items():
#         print('v', v)
#         count += v * (v - 1) // 2
#     return count
#
#
# # 入力
# N = int(input())
# A = list(map(int, input().split()))
#
# # 平方数ペアの個数を求める
# print(count_squareful_pairs(A, N))
