
# 섹션 3. 탐색&시뮬레이션.pdf
# 사과나무
# n*n 배열
# n의 크기는 항상 홀수
# 5 * 5 일때 n의 홀수 크기의 전체 합을 구해라

# a[i]~a[j] 행까지 합치는 문제

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/7) 사과나무"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]  # 1행씩 5번씩 읽어들이는 방법

res = 0
s = e = n // 2
# s = e = n//2 2로 나눈 몫은 2.. n이 5일때 배열의 수는 0~4이므로 가운데는 2가 됨..s
# 문제 포인트는 항상 홀수 라는 점 n = 항상 홀수

# 7 - 0123456
for i in range(n):
    for j in range(s, e + 1):  # j값은 0~1까지
        res += a[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
