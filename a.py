import sys
read = sys.stdin.readline
from collections import defaultdict

# エラトステネスの篩を用いてn以下の最小素因数を格納した配列を返す
def sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

# xを素因数分解する
def factorize(x, spf):
    res = []
    while x != 1:
        factor = spf[x]
        count = 0
        while x % factor == 0:
            x //= factor
            count += 1
        res.append([factor, count])
    return res

N = int(read())
l = list(map(int, read().split()))
spf = sieve(max(l))

# 奇数回出現する素因数のリスト
odd_factor_lists = []
for num in l:
    if num != 0:
        factors_with_exponents = factorize(num, spf)
        of = []
        for factor, exponent in factors_with_exponents:
            if exponent % 2 != 0:
                of.append(factor)
        odd_factor_lists.append(of)

# 奇数回出現する素因数のパターンに基づくカウント
odd_factors_count = defaultdict(int)
for odd_factors_list in odd_factor_lists:
    pattern = tuple(odd_factors_list)
    odd_factors_count[pattern] += 1

zero_count = l.count(0)
# 0と0以外の要素のペアの数と0同士のペアの数をカウント
count = zero_count * (N - zero_count) + zero_count * (zero_count - 1) // 2
# 奇数回出現する素因数のパターンに基づくペアの数をカウント
for v in odd_factors_count.values():
    count += v * (v - 1) // 2
print(count)



# # エラトステネスの篩を使用して最小の素因数を求める関数
# def sieve(n):
#     spf = list(range(n + 1))
#     for i in range(2, int(n ** 0.5) + 1):
#         if spf[i] == i:
#             for j in range(i * i, n + 1, i):
#                 if spf[j] == j:
#                     spf[j] = i
#     return spf
#
#
# # 素因数分解を行い、各素因子の指数が奇数のものだけを取り出す関数
# def factorize(n, spf):
#     factors = defaultdict(int)
#     while n > 1:
#         factors[spf[n]] += 1
#         n //= spf[n]
#     return [p for p, exp in factors.items() if exp % 2 == 1]
#
#
# # メインの処理
# def count_squareful_pairs(A, N):
#     spf = sieve(max(A))
#     factor_count = defaultdict(int)
#     zero_count = 0
#
#     for a in A:
#         if a == 0:
#             zero_count += 1
#             continue
#         print("factorize(a, spf)", factorize(a, spf))
#         pattern = tuple(sorted(factorize(a, spf)))
#         factor_count[pattern] += 1
#
#     print("factor_count", factor_count)
#     count = zero_count * (N - zero_count) + zero_count * (zero_count - 1) // 2
#     for k, v in factor_count.items():
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
