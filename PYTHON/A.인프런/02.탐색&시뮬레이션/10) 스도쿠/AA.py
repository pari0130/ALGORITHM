
# 섹션 3. 탐색&시뮬레이션.pdf

'''
# 코드작성 팁
ch 0으로 초기화 한 9개 길이 list 
행체크, 열체크, 그룹체크 에 대한 각각 list
각 행 열 그룹을 돌면서 ch list에 1~9 숫자가 있으면 1을 채워서 합의 값이 9가 되면 true
'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/10) 스도쿠"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# 배열 전체에 상하좌우 0 추가
n = int(input())  # 배열길이
a = [list(map(int, input().split())) for _ in range(n)]  # n*n 배열
