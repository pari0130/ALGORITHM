
# 섹션 4. 이분탐색 and 그리디.pdf

'''
DVD에는 총 N개의 곡이

즉, 1번 노래와 5번
노래를 같은 DVD에 녹화하기 위해서는 1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야
한다. 또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.

M개의 DVD에 모든 동영상을 녹화하기
로 하였다. 이 때 DVD의 크기(녹화 가능한 길이)를 최소로

M개의 DVD는
모두 같은 크기

입력받은 숫자 리스트를 원하는 크기 3장으로 만들기 위한 최소 합

lt = 1, rt = list 최대합
n는 9 list, m = 원하는 3장

lt=1, rt=45 

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/3) 뮤직비디오(결정알고리즘)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")


def Count(capacity):
    # list를 합처서 mid값을 넘가는지 체크 해야함
    # m장의 수를 넘어가면 false return
    cnt = 1
    sum = 0
    for x in Music:
        # 뮤직 리스트를 돌면서 sum 값을 더해주고, 더해준 sum 값이 mid를 넘어서는 순간 cnt (m으로 사용될) 값 증가, sum = 넘어온 x로 초기화
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
Music = list(map(int, input().spl()))
maxx = max(Music)  # list 원소 중 최대 값
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2  # 이분검색을 위한 중간 값의 몫
    # mid 값이 m장을 만들기 위한 조건을 충족하는가, 3장안에 포함되는가
    if mid >= maxxx and Count(mid) <= m:
        res = mid
        rt = mid - 1  # m장안에 속하므로 답이될수 있는 mid값이고, rt는 더 좁혀서 계산해보기 위해 mid -1로
    else:
        lt = mid + 1  # m장안에 속하지 않으므로 답이될수 없음. lt의 위치를 이동
