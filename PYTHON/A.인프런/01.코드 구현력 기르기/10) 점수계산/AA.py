
# 섹션 2. 코드 구현능력 기르기.pdf
# 10
# 0 1 0 0 1 0 1 1 0 0

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/01.코드 구현력 기르기/10) 점수계산"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for x in a:
    if x == 1:  # 연동적인 1의 경우 가중치 증가
        cnt += 1
        sum += cnt

    else:
        cnt = 0

print(sum)
