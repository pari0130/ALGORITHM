
# 섹션 2. 코드 구현능력 기르기.pdf
#

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/01.코드 구현력 기르기/4) 대표값"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")
n = int(input())
a = list(map(int, input().split()))

# 소수 첫째자리 반올림 하는 평균 초기화
# ave = round(sum(a) / n)
# 파이썬 라운드는 반 내림 방식을 택하므로 잘못되어 있음 0.5를 더한 후 반내림 을 하면 됨
ave = int((sum(a) / n) + 0.5)
min = 2147000000  # 정수형에 가장 큰 숫자

# list의 index와 실제 값을 가저오는 enumerate(a)
for idx, x in enumerate(a):
    tmp = abs(x - ave)  # 평균에 가장 가까운 점수와 idx를 구하는게 답
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:  # 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로
            score = x
            res = idx+1  # 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로

print(ave, res)

# 파이썬 라운드는 반 내림 방식을 택하므로 잘못되어 있음 0.5를 더한 후 반내림 을 하면 됨
a = 66.5
a = a + 0.5
a = int(a)
