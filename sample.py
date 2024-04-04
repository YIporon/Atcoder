#
#  受け取り
#
import sys
# String受け取り改行コード削除
S = input().strip()

# Int受け取り
A = int(sys.stdin.readline())
# 空白区切りInt受け取り
A, B = map(int, sys.stdin.readline().split())
# 空白区切りIntList受け取り
l = list(map(int, sys.stdin.readline().split()))
# 標準入力からA個の整数B_iを読み込んでリストに格納する
lb= [int(input()) for _ in range(A)]

# 二次元配列受け取り
H, W = map(int, sys.stdin.readline().split())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

#
# String
#

# 文字列Sの3文字目までを取得
S[:3] #=> S[0]S[1]S[2]を出力


#
# List
#

# '101'→[1,0,1]
s = input()
l = [int(char) for char in s]

# List降順
l.sort(reverse=True)
# 1から5までを出力
for i in range(1, 6):
    print(i)


# ListループIndex
for index, num in enumerate(l):
    break
# List結合
"".joins(l)

# List合計
sum(l)

# 二次元配列の横要素合計、縦要素合計
l[[1, 2, 3][2, 3, 4]]  # 二次元配列
yoko = list(map(sum, l))
tate = list(map(sum, zip(*l)))

# 主に複数のイテラブル（リスト、タプル、文字列など）から同じインデックスにある要素をグループ化して、新しいイテレータを生成する
zip(*l)

#
# Int
#
# 浮動小数点 2.0
s = 4 / 2

# 切り捨て除算 2
n = 5 / 2

#
# 便利関数(組み込み外)
#

# 各桁の和を計算する関数
def digit_sum(n):
    return sum(int(digit) for digit in str(n))


# 単なる素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr
factorization(24)
## [[2, 3], [3, 1]]


# エラトステネスの篩を用いてn以下の最小素因数を格納した配列を返す
def sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
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

#
# 2分探索
#
import bisect
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
bisect.bisect(a,55) #=>5
b = [1,2,2,2,3]
bisect.bisect_left(b,2) #=>1
bisect.bisect_right(a,2) #=> 4
bisect.bisect(a,2) #=> 4


#
# math
#

# ルートの作成方法
import math
math.sqrt(25) # =>5