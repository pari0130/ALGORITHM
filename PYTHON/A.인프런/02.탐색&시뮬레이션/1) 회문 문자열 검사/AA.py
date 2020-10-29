
# 섹션 3. 탐색&시뮬레이션.pdf
# 앞으로 뒤로 읽어도 같은 문자일 경우가 회문 문자열 임 level / moon

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/02.탐색&시뮬레이션/1) 회문 문자열 검사"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())

# 문자열 비교는 1-5 비교 2-4비교 이런식으로 끝과 끝 부분만 비교하면 같은지 알 수 있음.
# 개인적 생각은 역정렬이 필요할까 했지만 아님

# case 1 : 알고리즘 스럽게 짜려면 이와 같이
for i in range(n):
    s = input()
    s = s.upper()  # 대문자와 시킴
    size = len(s)  # 문자열 길이

    # print(s[-1])  # 파이썬에서는 마지막 배열을 -1로 접근 가능함
    for j in range(size // 2):
        if s[j] != s[-1 - j]:  # -1이 마지막 배열, -j 하는 이유는 마지막 배열에서 첫번쨰 배열의 길이만큼 추가로 빼주면서 길이 검증
            print("#%d NO" % (i + 1))
            break
    else:
        print("#%d YES" % (i + 1))

'''
# case 2 :
for i in range(n):
    s = input()
    s = s.upper()
    # if s == s[::-1]
    # print(s[::-1]) # 파이썬은 :: -1로 역정렬 해서 문자 확인이 가능함
    if s == s[::-1]:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))
'''
