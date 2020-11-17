
# 섹션 4. 이분탐색 and 그리디.pdf

'''
5
172 67
183 65
180 70
170 72
181 60

183 65
181 60
180 70
172 67
170 72

1. sort로 0번 index에 대한 키순을 내림차순으로 정렬
2. 1번 index 몸무게에 대한 body list를 증가 시키면서 큰값이 있으면 largest에 입력
3. 출력

해당 문제는 0번 index는 무조건 큰순으로 정렬시키면 1번 index만 비교해서 큰값을 찾는게 해답. 

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/6) 씨름선수(그리디-최적/탐욕 알고리즘)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))

body.sort(reverse=True)  # 첫번째 자리에 의해 내림차순 정렬 됨, 첫번째 값인 키에대한 정렬이 완료
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        cnt += 1
        largest = y  # 큰값

print(cnt)
