import sys

# 入力の読み取り
N, M = map(int, sys.stdin.readline().split())  # NとMを読み取る
Al = list(map(int, sys.stdin.readline().split()))  # N個の整数を読み取ってリストAlに格納
Bl = list(map(int, sys.stdin.readline().split()))  # M個の整数を読み取ってリストBlに格納

# リストのソート
Al.sort()  # リストAlを昇順にソート
Bl.sort()  # リストBlを昇順にソート

ans = 0  # 結果の累積和を保存する変数

# Blの各要素bについて処理を行う
for b in Bl:
    found = False  # 条件を満たすAlの要素が見つかったかどうかのフラグ

    # Alの各要素aについてb以上の要素を探す
    for idx, a in enumerate(Al):
        if found:
            break  # 条件を満たす要素が見つかったのでループを終了
        if a >= b:
            found = True  # 条件を満たす要素が見つかった
            ans += a  # 条件を満たす要素を累積和に加算
            Al = Al[idx+1:]  # Alを更新して、使用済みの要素を除去

    if not found:
        # 条件を満たす要素が見つからなかった場合
        print(-1)  # -1を出力
        exit()  # プログラムを終了

# 最終的な累積和を出力
print(ans)
