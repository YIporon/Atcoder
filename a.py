import sys
read = sys.stdin.readline
from bisect import bisect_right

N = int(read())
A = list(map(int, read().split()))
Q = int(read())

A.sort()
# クエリを処理する
for _ in range(Q):
    query = list(map(int, read().split()))
    if query[0] == 1:
        # クエリタイプ1: 数列 A 内の x の直後に y を挿入
        x, y = query[1], query[2]
        idx = bisect_right(A, x)
        A.insert(idx, y)

    elif query[0] == 2:
        # クエリタイプ2: 数列 A 内の x を削除
        x = query[1]
        A.remove(x)

# 処理後の数列 A を出力
print(*A)