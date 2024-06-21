import sys
import math

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

cnt = 0
for index, Ai in enumerate(A):
    cnt += abs(B[index] - Ai)

if cnt > K:
    print("No")
    sys.exit()

if (K - cnt) % 2 == 0:
    print("Yes")
else:
    print("No")
