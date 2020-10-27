
# 섹션 2. 코드 구현능력 기르기.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/01.코드 구현력 기르기/7) 소수의 개수(에라토스테네스 체)"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")
n = int(input())
ch = [0] * (n + 1)
cnt = 0
for i in range(2, n):  # 소스는 1이상 부터 1과 자기자신의 약수만 가지는 수
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):  # 2가 들어올 경우 2의 배수를 증가 시키면서 1로 바꿈 (0인 경우만 샐 수 있도록)
            ch[j] = 1

print(cnt)
