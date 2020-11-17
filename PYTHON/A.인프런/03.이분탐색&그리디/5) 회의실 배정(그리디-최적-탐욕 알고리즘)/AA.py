
# 섹션 4. 이분탐색 and 그리디.pdf

'''
5
1 4
2 3
3 5
4 6
5 7
'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/5) 회의실 배정(그리디)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())  # 회의실 현황표의 시작/끝 시간 입력값
    meeting.append((s, e))  # 튜플 형태 매핑

meeting.sort(key=lambda x: (x[1], x[0]))  # x[0]이 우선순위, x[1]이 차순이 되게 정렬

et = 0
cnt = 0
for s, e in meeting:
    if s >= et:  # 회의실 시작/종료 시간이 있으며 앞의 list 튜플이 1,4 일때 다음 튜플이 4보다 큰지 비교하는 값임
        et = e
        cnt += 1

print(cnt)
