
# 섹션 2. 코드 구현능력 기르기.pdf
#

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/01.코드 구현력 기르기/5) 정다면체"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")
n, m = map(int, input().split())

cnt = [0] * (n + m + 3)  # list 초기화
max = -2147000000  # 정수 가장 작은 값 초기화

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=' ')
