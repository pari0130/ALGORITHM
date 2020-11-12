
# 섹션 4. 이분탐색 and 그리디.pdf
# 이분 탐색은 전체 길이를 절반씩 자르면서 ( mid = rt // lt) 구하려는 값과 인덱스 값을 비교하여 크고 작음에 따라
# 계속 절반씩 잘라가며 답을 찾는 과정임

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/1) 이분탐색"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n, m = map(int, input().split())  # n = list 길이 m = 찾으려는 값
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = n-1

while lt <= rt:
    mid = (lt + rt) // 2  # 1. 이분탐색 절반 찾기
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:  # 2. list의 현재 index값이 찾으려는 m 값 보다 큰지 비교 후 mid 가 크면 mid 크기를 줄이고
        rt = mid - 1
    else:  # 3. 그렇지 않을경우 - a[mid]  < m 일 경우에는 절반의 위치는 mid+1
        lt = mid+1
