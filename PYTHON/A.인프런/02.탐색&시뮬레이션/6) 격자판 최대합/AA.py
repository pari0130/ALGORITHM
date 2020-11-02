
# 섹션 3. 탐색&시뮬레이션.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/5) 수의 합"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())
max = 0

# 1. 가로 5개 더하고
# 2. 세로 5개 더하고
# 3. 가로1 세로+1 가로+1 해서 대각선 더해서 합
