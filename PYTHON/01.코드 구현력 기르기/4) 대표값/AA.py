
# 섹션 2. 코드 구현능력 기르기.pdf

import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/01.코드 구현력 기르기/4) 대표값"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
