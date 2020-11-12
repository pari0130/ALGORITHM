
# 섹션 4. 이분탐색 and 그리디.pdf

'''
최대 길이는 입력받은 가장 큰수가 기준이 된다.
n, m 일때 m의 개수보다 크면 일단 tmp = int num save


'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/2) 랜선 자르기(결정알고리즘)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")


def Count(len):  # mid 값을 받아서
    cnt = 0
    for x in Line:  # 4. 전달 받은 line 수 만큼 for 돌면서
        cnt += (x // len)  # 5. line 을 나눈 몫을 구함
    return cnt


k, n = map(int, input().split())  # k,n 4개의 길이와 필요한 11개 입력
Line = []  # 길이 저장할 변수
res = 0  # 적합한 길이
largest = 0  # 최대 길이 값

# 1. for문 실행 이유는 최대 길이 값을 기준으로 잘라서 갯수를 구해야 하기 때문에 입력받은 값 중 되대 길이를 찾으려고 for
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)  # 둘을 비교해서 큰 값을 담아 주는 max() 함수

# 이분검색 조건
lt = 1
rt = largest

while lt <= rt:  # 2. 이분검색 자를 수 있는 최대 값 까지 while
    mid = (lt + rt) // 2  # 중간값으로 이분 탐색 조건 생성
    if Count(mid) >= n:  # 3. mid 값 함수에 전달해서 n 필요한 11개보다 크거나 같을 경우 res 값을 mid 값으로 저장
        res = mid
        lt = mid+1  # 다음 값을 위해 lt 값 증가
    else:
        rt = mid - 1  # 6. 그밖에 구하려는 필요 값보다 작을 경우 rt 위치 이동

print(res)
