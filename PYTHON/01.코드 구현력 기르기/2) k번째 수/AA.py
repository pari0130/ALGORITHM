
# 섹션 2. 코드 구현능력 기르기.pdf
# 숫자 리스트 오름차순 정렬 후 입력받은 숫자 번째의 리스트 숫자 출력
# 6 2 5 3 ( 6개의 숫자 리스트, 2~5번째중, 3번째 숫자 출력)
# 5 2 7 3 8 9

import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/01.코드 구현력 기르기/2) k번째 수"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")

T = int(input())  # 첫번째줄 테스트 코드 숫자

for t in range(T):
    n, s, e, k = map(int, input().split())  # 4개의 숫자를 읽음
    a = list(map(int, input().split()))
    # print(a)  # index 위치 slice 1~5
    a = a[s - 1:e]
    a.sort()  # 오름차순 정렬
    # -1을 하는 이유는 입력받은 숫자 -1이 list의 index 이므로. 참고
    print("#%d %d" % (t+1, a[k-1]))
