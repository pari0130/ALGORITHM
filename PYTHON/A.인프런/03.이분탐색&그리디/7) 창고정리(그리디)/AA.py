
# 섹션 4. 이분탐색 and 그리디.pdf

'''
창고정리 
- 창고물품이 쌓여있는 10개 길이가 있고 창고물품이 10개 길이마다 숫자로 지정되어 있음
- 창고정리란 가장 높은숫자 물품을 가장 낮은곳으로 옮긴뒤 가장 높은곳과 낮은곳의 길이차이를 출력함
- l = 창고길이, list = 높음/낮음 숫자, m = 높이조정횟수

오름차순 소팅을 하면 가장낮은값과 가장높은값이 정렬되어 비교하기 쉽다

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/7) 창고정리(그리디)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

L = int(input())
a = list(map(int, input().split()))  # 입력받은 숫자 list
m = int(input())
a.sort()  # 창고길이 숫자 list를 오름차순 정렬

for _ in range(m):
    a[0] += 1  # 가장낮은 index 1 증가
    a[L - 1] -= 1  # 가장높은 index 1 감소
    a.sort()  # 증감이 완료되었으면 sort 조정

print(a[L-1] - a[0])  # 최정 결과값 = 초대길이 - 최소길이 출력
