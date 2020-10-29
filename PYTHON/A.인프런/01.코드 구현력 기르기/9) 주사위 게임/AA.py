
# 섹션 2. 코드 구현능력 기르기.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/01.코드 구현력 기르기/9) 주사위 게임"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")

n = int(input())
res = 0
money = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)  # 숫자 3개 list 매핑

    if a == b and b == c:  # 규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원
        money = 10000 + a * 1000

    elif a == b or a == c:  # 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원
        money = 1000 + (a*100)

    elif b == c:  # 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원
        money = 1000 + (b * 100)

    else:  # 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원
        momey = c * 100

    if money > res:
        res = money

print(res)
