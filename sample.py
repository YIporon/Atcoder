#
#  受け取り
#
import sys
input = sys.stdin.readline

# String受け取り改行コード削除
S = input().strip()

# Int受け取り
A = int(input())
# 空白区切りInt受け取り
A, B = map(int, input().split())
# 空白区切りIntList受け取り
l = list(map(int, input().split()))

# 二次元配列受け取り
H, W = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(H)]


#
# List
#

# '101'→[1,0,1]
s = input()
l = [int(char) for char in s]


# List降順
l.sort(reverse = True)

# ListループIndex
for index, num in enumerate(l):
    break
# List結合
''.joins(l)

# List合計
sum(l)

# 二次元配列の横要素合計、縦要素合計
l [[1,2,3][2,3,4]] # 二次元配列
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
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
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
