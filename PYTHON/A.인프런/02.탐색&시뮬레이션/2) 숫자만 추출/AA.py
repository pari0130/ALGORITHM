
# 섹션 3. 탐색&시뮬레이션.pdf
# 처음이 0인 문자는 무시, 숫자를 구하고 약수 개수도 구해야함

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/2) 숫자만 추출"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

s = input()
res = 0
for x in s:  # s 문자 돌면서 알아서 추출 함
    if x.isdecimal():  # x.isdigit 은 숫자만 찾고 decimal 은 0~9 까지 찾음
        # 이 부분으로 인해 0의 첫 자리가 무시 될 수 있음
        # res 는 처음 0으로 인해 1번자리 그다음 10이자리 그다음 100의 자리를 차례로 구 할 수 있음
        res = res * 10 + int(x)

print(res)

cnt = 0
for i in range(1, res + 1):
    if res % i == 0:  # res 의 약수
        cnt += 1

print(cnt)
