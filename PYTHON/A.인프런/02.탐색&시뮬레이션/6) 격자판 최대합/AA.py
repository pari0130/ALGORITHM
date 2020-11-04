
# 섹션 3. 탐색&시뮬레이션.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/6) 격자판 최대합"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]  # 1행씩 5번씩 읽어들이는 방법

largest = -2147000000

# for x in a:  # a라는 2차원 list 의 x 1행
#     print(x)

for i in range(n):  # i 0번행을 돌고 i 1번행을 돌고 반복 하며 largest 값을 비교 저장 for문이 2중이라 헷갈릴 수 있음
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > largest:  # 행과 열의 최대 합이 sum에 저장
        largest = sum1

    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]  # 대각선을 찾아줌
    sum2 += a[i][n - i - 1]  # 0~4일때 n는 5이며 5-0-1 이 되도록 해야함

if sum1 > largest:  # 최대 합이 sum에 저장
    largest = sum1

if sum2 > largest:
    largest = sum2

print(largest)
