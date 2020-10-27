
# 섹션 2. 코드 구현능력 기르기.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/01.코드 구현력 기르기/6) 자릿수의 합"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")
n = int(input())
a = list(map(int, input().split()))
max = -2147000000  # 정수 가장 작은 값 초기화


def digit_sum(x):
    sum = 0
    # while x > 0:  # 125가 넘어왔을 경우
    #     sum += x % 10  # 125를 10으로 나눈 나머지 5 가  sum이 누적
    #     x = x // 10  # 125를 10으로 나눈 결과 12가 x 에 누적
    #     # 1 2 5에 대한 값이 sum이 됨
    # return sum
    for i in str(x):  # 스트링으로 접근하면 125 숫자를 1, 2, 5 하나씩 접근 가능함 tip
        sum += int(i)
    return sum


for x in a:
    tot = digit_sum(x)  # 합을 구하고
    if tot > max:  # max 값 보다 tot가 클 경우
        max = tot
        res = x

print(res)
